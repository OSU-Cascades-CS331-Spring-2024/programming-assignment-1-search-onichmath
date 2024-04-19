import math

class City:
    def __init__(self, name, longitude, latitude):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return self.name

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude

    def get_cartesian_coordinates(self):
        return self.polar_to_cartesian(self.longitude, self.latitude)

    @staticmethod
    def polar_to_cartesian(longitude, latitude):
        x = math.cos(math.radians(latitude)) * math.cos(math.radians(longitude))
        y = math.cos(math.radians(latitude)) * math.sin(math.radians(longitude))
        z = math.sin(math.radians(latitude))
        return x, y, z


    @staticmethod
    def degrees_to_decimal(degrees, minutes, seconds, direction):
        if direction in ['S', 'W']:
            return -1 * (float(degrees) + float(minutes) / 60 + float(seconds) / 3600)
        return float(degrees) + float(minutes) / 60 + float(seconds) / 3600

    @classmethod
    def from_string(cls, string):
        parts = string.split(" --> ")

        city_info = parts[0].split()
        name = city_info[0]
        lat_degrees, lat_minutes, lat_seconds, lat_direction = city_info[1:5]
        lon_degrees, lon_minutes, lon_seconds, lon_direction = city_info[5:]

        latitude = float(lat_degrees) + float(lat_minutes) / 60 + float(lat_seconds) / 3600
        longitude = float(lon_degrees) + float(lon_minutes) / 60 + float(lon_seconds) / 3600

        print(name, longitude, latitude)
        return cls(name, longitude, latitude)

