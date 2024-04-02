import geocoder

def obtener_coordenadas_ubicacion_actual():
    ubicacion = geocoder.ip('me')
    if ubicacion:
        print("Las coordenadas de tu ubicación actual son:")
        print("Latitud:", ubicacion.latlng[0])
        print("Longitud:", ubicacion.latlng[1])
    else:
        print("No se pudo determinar tu ubicación actual.")

def Longitude():
    print(geocoder.ip('me').latlng[1])
    return geocoder.ip('me').latlng[1]

def Latitude():
    print(geocoder.ip('me').latlng[0])
    return geocoder.ip('me').latlng[0]
