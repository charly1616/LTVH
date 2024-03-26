from typing import Any, Optional, Union
from flet import *
from Flet_map import FletMap
import GPS
import time
from flet_core.types import (
    AnimationValue,
    OffsetValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
)

class NavegableMap(Container):
    def __init__(
            self,
            #COMPONENTES PARTICULARES QUE QUIZAS PUEDES TOCAR
            width:int = 600,
            height:int = 600,
            iniZoom:int = 6,
            iniLat:float = 10,
            iniLong:float = -70,
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
        self.MapN = 5
        self.height = height
        self.width = width
        self.iniZoom = iniZoom
        self.iniLat = iniLat
        self.iniLong = iniLong

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
        move_right = FilledButton(text=">",on_click=lambda _: self._moveMap(tutu=360/(2**self.iniZoom)))
        move_left = FilledButton(text="<",on_click=lambda _: self._moveMap(tutu=-360/(2**self.iniZoom)))
        move_down = FilledButton(text="↑",on_click=lambda _: self._moveMap(lala=360/(2**self.iniZoom)))
        move_up = FilledButton(text="↓",on_click=lambda _: self._moveMap(lala=-360/(2**self.iniZoom)))
        zoom_in = FilledButton(text="+",on_click=lambda _: self._moveMap(zoom_change=1))
        zoom_out = FilledButton(text="-",on_click=lambda _: self._moveMap(zoom_change=-1))
        up_and_down = Column(spacing=0,controls=[move_down,move_up]) #El boton de arriba y abajo unidos
        directions = Row(spacing=0,controls=[move_left,up_and_down,move_right]) #Boton de direcciones unido

        zooms = Row(spacing=0,controls = [zoom_in,zoom_out]) #Union de los dos zoom
        
        move = Row(width= self.width,alignment=MainAxisAlignment.SPACE_BETWEEN,controls=[directions,zooms])#Union de los zoom y las direcciones, expandidos
        self.content = Column(controls=[move,self.map_view]) #Contenido del componente
        pass


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
    nav = NavegableMap(width=800,height=800,iniZoom=19)
    page.add(nav)

app(target=main)
