import math
import sys

class City:
    def __init__(self, name, longitude, latitude, connections):
        """
        Initializes a city with a name, longitude, and latitude
        """
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.connections = connections

    def __str__(self):
        """
        Returns the name of the city
        """
        return self.name

    def __repr__(self):
        """
        Returns a string representation of the city
        """
        return f"City(name={self.name}, latitude={self.latitude}, longitude={self.longitude}, connections={self.connections})"

    def get_longitude(self):
        """
        Returns the longitude of the city
        """
        return self.longitude

    def get_latitude(self):
        """
        Returns the latitude of the city
        """
        return self.latitude

    def get_cartesian_coordinates(self):
        """
        Returns the cartesian coordinates of the city
        """
        return self.polar_to_cartesian(self.longitude, self.latitude)

    @staticmethod
    def polar_to_cartesian(longitude, latitude):
        """
        Converts spherical polar coordinates to cartesian coordinates
        """
        x = math.cos(math.radians(latitude)) * math.cos(math.radians(longitude))
        y = math.cos(math.radians(latitude)) * math.sin(math.radians(longitude))
        z = math.sin(math.radians(latitude))
        return x, y, z

    @staticmethod
    def degrees_to_decimal(degrees, minutes, seconds, direction):
        """
        Converts degrees, minutes, seconds to decimal degrees
        """
        if direction in ['S', 'W']:
            return -1 * (float(degrees) + float(minutes) / 60 + float(seconds) / 3600)
        return float(degrees) + float(minutes) / 60 + float(seconds) / 3600

    @classmethod
    def from_string(cls, string):
        """
        Creates a city object from a string
        """
        parts = string.split(" --> ")

        city_info = parts[0].split()
        name = city_info[0]

        lat_degrees, lat_minutes, lat_seconds, lat_direction = city_info[1:5]
        lon_degrees, lon_minutes, lon_seconds, lon_direction = city_info[5:]

        latitude = cls.degrees_to_decimal(lat_degrees, lat_minutes, lat_seconds, lat_direction)
        longitude = cls.degrees_to_decimal(lon_degrees, lon_minutes, lon_seconds, lon_direction)

        connections_info = parts[1].split()
        connections = {connections_info[i]: float(connections_info[i + 1]) for i in range(0, len(connections_info), 2)}
    
        return cls(name, longitude, latitude, connections) 

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: python city_string")
        sys.exit(1)
    string = sys.argv[1]
    city = City.from_string(string)
    print(repr(city))
