from typing import Any, Optional, Union
import math
from flet import * 
from flet_core import alignment
import flet_core as ft
from flet_core.container import Container
from flet_core.control import OptionalNumber
import flet.canvas as cv
from flet_core import control
from flet_core.image import Image
from flet_core.ref import Ref
from flet_core.row import Row
from flet_core.column import Column
from flet_core.types import (
    AnimationValue,
    OffsetValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
)
 

points = [[153234,246072,100,16],[153235,246072,16,16],[153234,246073,16,16],[153235,246073,16,16],[153187,246054,110,20],[153227,246121,40,170],[152067,248212,100,100]]


class FletMap(Container):
    def __init__(
        self,
        height: int = 200,
        width: int = 200,
        NoNumbers: bool = False,
        ref: Optional[Ref] = None,
        expand: Union[None, bool, int] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        aspect_ratio: OptionalNumber = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        on_animation_end=None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
        #
        # Specific
        #
        screenView: Optional[list] = [],
        latitude: Optional[float] = 0.0,
        longtitude: Optional[float] = 0.0,
        delta_lat: Optional[float] = 0.0,
        delta_long: Optional[float] = 0.0,
        zoom: Optional[float] = 0.0,
        isolated: bool = False,
        original_size: bool = False,
        transparent: bool = False,
    ):
 
        Container.__init__(
            self,
            ref=ref,
            expand=expand,
            col=col,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            tooltip=tooltip,
            visible=visible,
            disabled=disabled,
            data=data,
        )
 
        self.latitude = latitude
        self.longtitude = longtitude
        self.delta_lat = delta_lat
        self.delta_long = delta_long
        self.zoom = zoom
        self.screenView = screenView
        self.isolated = isolated
        self.original_size = original_size
        self.transparent = transparent
        self.height = height
        self.width = width
        self.__canvas = cv.Canvas(shapes=[],width=self.width,height=self.height)
        self.NoNumbers = NoNumbers
 
    def _is_isolated(self):
        return self.__isolated
 
    def _build(self):
        self.alignment = alignment.center
        self.__row = Row()
        self.__col = Column()
        # self.content
        # self.content = self.__img
    


    def _get_image_cluster(self):
        self.__canvas.shapes=[]
        index = 0
        smurl = r"http://tile.openstreetmap.org/{0}/{1}/{2}.png"
        
        shapies = []
        xmin, ymax = self.deg2num(self.latitude, self.longtitude, self.zoom)
        xmax, ymin = self.deg2num(self.latitude + self.delta_lat, self.longtitude + self.delta_long, self.zoom)
        self.__row = Row(spacing=1, auto_scroll=True)
        ex,uy = 0,0 #GridPosition for canvas
        for xtile in range(xmin, xmax+self.screenView[0]):
            self.__col = Column(spacing=1, auto_scroll=True)
            uy=0
            for ytile in range(ymin,  ymax+self.screenView[1]):

                try:
                    imgurl = smurl.format(self.zoom, xtile if xtile < 2**self.zoom else xtile - 2**self.zoom, ytile if ytile < 2**self.zoom else ytile-2**self.zoom)
                    #print(str(xtile if xtile < 2**self.zoom else xtile - 2**self.zoom)," - ",str(ytile))
                    pow=2**(19-self.zoom)
                    for a in points:
                        if int(a[0]/pow) == xtile and int(a[1]/pow) == ytile:
                            xboxpercent = self.width/self.screenView[1] * (a[0]/pow - int(a[0]/pow))
                            yboxpercent = self.height/self.screenView[0] * (a[1]/pow - int(a[1]/pow))
                            shapies.append(cv.Circle(int(ex*self.width/4 + a[2]/pow + xboxpercent), int(uy*self.height/4 + a[3]/pow + yboxpercent), 5, Paint(style=ft.PaintingStyle.FILL)))
                            #print(int(ex*self.width/4 + a[2]), int(uy*self.height/4 + a[3]),ex,uy)
                    self.__col.controls.append(
                        Stack(controls=[Image(height=self.height/self.screenView[0] ,width=self.width/self.screenView[1],src=imgurl),
                                        Text(value= ' ' if self.NoNumbers else (str(xtile if xtile < 2**self.zoom else xtile - 2**self.zoom)+" - "+str(ytile)) ,size = 10)]))
                except:
                    print("Couldn't download image")
                uy+=1
            self.__row.controls.append(self.__col)
            ex+=1
        #print()
        #print(shapies)
        self.__canvas.shapes = shapies
        self.content = Stack(controls=[self.__row,self.__canvas])
 
    def _before_build_command(self):
        super()._before_build_command()
        # self.delta_lat = 0.5
        # self.delta_lon = 0.5
        self._get_image_cluster()
        # print(self.__src_content)
        # self.__img.src = self.__src_content
 
    def deg2num(self, lat_deg, lon_deg, zoom):
        lat_rad = math.radians(lat_deg)
        n = 2.0 ** zoom
        xtile = int((lon_deg + 180.0) / 360.0 * n)
        
        logPar = math.tan( lat_rad) + (1 / math.cos(lat_rad))
        #print('LatRad  ', lat_deg)
        #print('DATO QUE JODE   ',logPar)
        ytile = int((1.0 - math.log(abs(logPar)) / math.pi) / 2.0 * n)
        return (xtile, ytile)
 
    def num2deg(self, xtile, ytile, zoom):
        n = 2.0 ** zoom
        lon_deg = xtile / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
        lat_deg = math.degrees(lat_rad)
        return (lat_deg, lon_deg)
 
    # zoom
    @property
    def zoom(self):
        return self.__zoom
 
    @zoom.setter
    def zoom(self, value):
        self.__zoom = value
 
    # delta_long
    @property
    def delta_long(self):
        return self.__delta_long
 
    @delta_long.setter
    def delta_long(self, value):
        self.__delta_long = value
 
    # delta_lat
    @property
    def delta_lat(self):
        return self.__delta_lat
 
    @delta_lat.setter
    def delta_lat(self, value):
        self.__delta_lat = value
 
    # latitude
    @property
    def latitude(self):
        return self.__latitude
 
    @latitude.setter
    def latitude(self, value):
        self.__latitude = value
 
    # longtitude
    @property
    def longtitude(self):
        return self.__longtitude
 
    @longtitude.setter
    def longtitude(self, value):
        self.__longtitude = value
 
    # original_size
    @property
    def original_size(self):
        return self.__original_size
 
    @original_size.setter
    def original_size(self, value):
        self.__original_size = value
 
    # isolated
    @property
    def isolated(self):
        return self.__isolated
 
    @isolated.setter
    def isolated(self, value):
        self.__isolated = value
 
    # maintain_aspect_ratio
    @property
    def maintain_aspect_ratio(self) -> bool:
        return self.__maintain_aspect_ratio
 
    @maintain_aspect_ratio.setter
    def maintain_aspect_ratio(self, value: bool):
        self.__maintain_aspect_ratio = value
 
    # transparent
    @property
    def transparent(self) -> bool:
        return self.__transparent
 
    @transparent.setter
    def transparent(self, value: bool):
        self.__transparent = value

    

