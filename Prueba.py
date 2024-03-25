from flet import *
from Flet_map import FletMap
import GPS
import time

global longi
longi = 10.98017#GPS.Longitude()
global lat
lat = -74.81540#GPS.Latitude()

def main(page: Page):
    global longi
    global lat
    page.title = "Olga No Trabaja"
    initial_zoom = 5
    MapN = 10

    map_view = FletMap(
            height=800,
            width=800,
            expand=False,
            latitude=lat,
            longtitude=longi,
            zoom=initial_zoom ,
            screenView=[MapN, MapN]
        )


    def moveMap(tutu = 0,lala = 0):
        global longi
        global lat
        if tutu > 0:
            longi = longi+tutu if longi+tutu < 360 else longi-360+tutu
        else:
            longi = longi+tutu if longi+tutu > -360 else longi+360+tutu
        if lala > 0:
            lat = lat+lala if lat+lala < 360 else lat-360+lala
        else:
            lat = lat+lala if lat+lala > -360 else lat+360+lala
        print(longi)
        mp = FletMap(
            height=800,
            width=800,
            expand=False,
            latitude=lat,
            longtitude=longi,
            zoom=initial_zoom ,
            screenView=[MapN, MapN]
        )
        page.controls[0].controls.pop()
        page.controls[0].controls.insert(1,mp)
        page.update()

    d = Container(content=FilledButton(text=">"),on_click=lambda _: moveMap(tutu=36))
    a = Container(content=FilledButton(text="<"),on_click=lambda _: moveMap(tutu=-36))
    s = Container(content=FilledButton(text="↑"),on_click=lambda _: moveMap(lala=36))
    w = Container(content=FilledButton(text="↓"),on_click=lambda _: moveMap(lala=-36))
    move = Row(controls=[a,w,s,d])
    page.add(Column(scroll='auto',controls=[move,map_view]))


# Olgota: [10.98017, -74.81540]
# Juanda: [9.5214, -75.58337]
app(target=main)
