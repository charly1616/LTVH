import geocoder

class GPS:
    def Longitude():
        ubicacion = geocoder.ip('me')
        if ubicacion:
            return ubicacion.latlng[1]
        else:
            return -74.78

    def Latitude():
        ubicacion = geocoder.ip('me')
        if ubicacion:
            return ubicacion.latlng[0]
        else:
            return 10.96

