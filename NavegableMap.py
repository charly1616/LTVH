from typing import Any, Optional, Union
from flet import *
from Flet_map import FletMap
import flet.canvas as cv
from GPS import GPS as g
import time
from flet_core.types import (
    AnimationValue,
    OffsetValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
)

points = [[153234, 246072, 16,18]]

class NavegableMap(Container):
    def __init__(
            self,
            #COMPONENTES PARTICULARES QUE QUIZAS PUEDES TOCAR
            width:int = 600,
            height:int = 600,
            iniZoom:int = 6,
            iniLat:float = 10,
            iniLong:float = -74,
            WhiteBg: bool = True,
            MenuCol: str = 'red',
            #COMPONENTES GENERALES QUE NO HAY QUE TOCAR
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
    ):  
        #INICIALIZACION DEL CONTENEDOR
        Container.__init__(self,
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
        self.MapN = 4
        self.height = height + 73
        self.width = width + 3
        self.iniZoom = iniZoom
        self.iniLat = iniLat
        self.iniLong = iniLong
        self.WhiteBg = WhiteBg
        self.MenuCol = MenuCol

        #Mapa inicial
        self.map_view = FletMap(
            height=width,
            width=width,
            expand=False,
            latitude=self.iniLat,
            longtitude=self.iniLong,
            zoom=self.iniZoom ,
            screenView=[self.MapN, self.MapN]
        )

        #La creacion de las flechas y los botones de zoom
        move_right = IconButton(height=50,icon=icons.ARROW_RIGHT,on_click=lambda _: self._moveMap(tutu=360/(2**self.iniZoom)))
        move_left = IconButton(height=50,icon=icons.ARROW_LEFT,on_click=lambda _: self._moveMap(tutu=-360/(2**self.iniZoom)))
        move_up = IconButton(height=35 ,icon=icons.ARROW_DROP_DOWN_SHARP,on_click=lambda _: self._moveMap(lala=-360/(2**self.iniZoom)))
        move_down = IconButton(height=35 ,icon=icons.ARROW_DROP_UP_SHARP,on_click=lambda _: self._moveMap(lala=360/(2**self.iniZoom)))
        zoom_in = IconButton(height=50,icon=icons.ZOOM_IN_ROUNDED,on_click=lambda _: self._moveMap(zoom_change=1))
        zoom_out = IconButton(height=50,icon=icons.ZOOM_OUT_ROUNDED,on_click=lambda _: self._moveMap(zoom_change=-1))
        up_and_down = Column(spacing=0,controls=[move_down,move_up]) #El boton de arriba y abajo unidos
        directions = Row(spacing=0,controls=[move_left,up_and_down,move_right]) #Boton de direcciones unido
        ubication = IconButton(height=50,icon=icons.ZOOM_OUT_ROUNDED,on_click=lambda _: self.changePosition(g.Longitude(),g.Latitude()))
        zooms = Row(spacing=0,controls = [zoom_in,zoom_out]) #Union de los dos zoom
        
        move = Container(bgcolor=self.MenuCol,
                         content = Row(width= self.width,alignment=MainAxisAlignment.SPACE_BETWEEN,controls=[directions,ubication,zooms]))#Union de los zoom y las direcciones, expandidos
        self.content = Column(width=200,spacing=0,controls=[move,self.map_view]) #Contenido del componente
        self.bgcolor = 'white' if self.WhiteBg else 'red'
        pass

    def changePosition(self, lo,la):
        self.iniLong = lo
        self.iniLat = la
        mp = FletMap(
            height=self.width,
            width=self.width,
            expand=False,
            latitude=self.iniLat,
            longtitude=self.iniLong,
            zoom=self.iniZoom ,
            screenView=[self.MapN, self.MapN]
        )
        self.content.controls.pop()
        self.content.controls.insert(1,mp)
        self.update() #ACTUALIZA EL COMPONENTE

    #Funcion que mueve el mapa y le hace zoom
    def _moveMap(self,tutu = 0  ,lala = 0  , zoom_change=0):
        if tutu > 0:
            self.iniLong = self.iniLong+tutu if self.iniLong+tutu < 360 else self.iniLong-360+tutu
        else:
            self.iniLong = self.iniLong+tutu if self.iniLong+tutu > -360 else self.iniLong+360+tutu
        if lala > 0:
            self.iniLat = self.iniLat+lala if self.iniLat+lala < 360 else self.iniLat-360+lala
        else:
            self.iniLat = self.iniLat+lala if self.iniLat+lala > -360 else self.iniLat+360+lala
        if self.iniZoom + zoom_change < 20 and self.iniZoom + zoom_change > 0: self.iniZoom += zoom_change
        
        mp = FletMap(
            height=self.width,
            width=self.width,
            expand=False,
            latitude=self.iniLat,
            longtitude=self.iniLong,
            zoom=self.iniZoom ,
            screenView=[self.MapN, self.MapN]
        )
        self.content.controls.pop()
        self.content.controls.insert(1,mp)
        self.update() #ACTUALIZA EL COMPONENTE



def main(page: Page):
    page.title = "Olga No Trabaja"
    nav =  Container(
        content=Column(
            controls = [
                NavegableMap(width=800,height=800,iniZoom=19),
                Container(
                        content=cv.Canvas(shapes = [
                        cv.Path(
                            [
                                cv.Path.MoveTo(25, 25),
                                cv.Path.LineTo(105, 25),
                                cv.Path.LineTo(25, 105),
                            ],
                            paint=Paint(
                                style=PaintingStyle.FILL,
                            ),
                        ),
                        cv.Path(
                            [
                                cv.Path.MoveTo(125, 125),
                                cv.Path.LineTo(125, 45),
                                cv.Path.LineTo(45, 125),
                                cv.Path.Close(),
                            ],
                            paint=Paint(
                                stroke_width=2,
                                style=PaintingStyle.STROKE,
                        ),
                    ),]
            ,width=600,height=600) ) ]
                    ))
    page.add(nav)

app(target=main)
