class City:
    def __init__(self, name, longitude, latitude, connections = []):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.connections = connections

    def __str__(self):
        return self.name

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude
