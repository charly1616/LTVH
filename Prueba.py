from flet import *
from Flet_map import FletMap
import GPS
import time

global longi
global lat
longi = -74.81540#GPS.Longitude()
lat = 10.98017#GPS.Latitude()
initial_zoom = 19
Length = 800
MapN = 5

def main(page: Page):
    global longi
    global lat
    global MapN
    page.title = "Olga No Trabaja"

    map_view = FletMap(
            height=Length,
            width=Length,
            expand=False,
            latitude=lat,
            longtitude=longi,
            zoom=initial_zoom ,
            screenView=[MapN, MapN]
        )


    def moveMap(tutu = 0,lala = 0, zoom_change=0):
        global longi
        global lat
        global initial_zoom
        if tutu > 0:
            longi = longi+tutu if longi+tutu < 360 else longi-360+tutu
        else:
            longi = longi+tutu if longi+tutu > -360 else longi+360+tutu
        if lala > 0:
            lat = lat+lala if lat+lala < 360 else lat-360+lala
        else:
            lat = lat+lala if lat+lala > -360 else lat+360+lala
        if initial_zoom + zoom_change < 20 and initial_zoom + zoom_change > 0: initial_zoom += zoom_change
        print(longi)
        mp = FletMap(
            height=Length,
            width=Length,
            expand=False,
            latitude=lat,
            longtitude=longi,
            zoom=initial_zoom ,
            screenView=[MapN, MapN]
        )
        page.controls[0].controls.pop()
        page.controls[0].controls.insert(1,mp)
        print('Zoom: ', initial_zoom)
        page.update()

    move_right = FilledButton(text=">",on_click=lambda _: moveMap(tutu=360/(2**initial_zoom)))
    move_left = FilledButton(text="<",on_click=lambda _: moveMap(tutu=-360/(2**initial_zoom)))
    move_down = FilledButton(text="↑",on_click=lambda _: moveMap(lala=360/(2**initial_zoom)))
    move_up = FilledButton(text="↓",on_click=lambda _: moveMap(lala=-360/(2**initial_zoom)))
    zoom_in = FilledButton(text="+",on_click=lambda _: moveMap(zoom_change=1))
    zoom_out = FilledButton(text="-",on_click=lambda _: moveMap(zoom_change=-1))

    up_and_down = Column(controls=[move_down,move_up])
    directions = Row(controls=[move_left,up_and_down,move_right])

    zooms = Row(controls = [zoom_in,zoom_out])
    
    
    move = Row(width= Length,alignment=MainAxisAlignment.SPACE_BETWEEN,controls=[directions,zooms])
    page.add(Column(scroll='auto',controls=[move,map_view]))


# Olgota: [10.98017, -74.81540]
# Juanda: [9.5214, -75.58337]
app(target=main)
