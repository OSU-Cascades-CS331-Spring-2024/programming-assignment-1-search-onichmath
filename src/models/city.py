import math
import sys

class City:
    def __init__(self, name, longitude, latitude, connections):
        """
        Initializes a city with a name, longitude, latitude, and connections
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

    def get_name(self):
        """
        Returns the name of the city
        """
        return self.name

    def get_cost(self, city:str):
        """
        Returns the cost of traveling to a city
        """
        return self.connections[city]

    def get_connections(self):
        """
        Returns the connections of the city
        """
        return self.connections

    @staticmethod
    def degrees_to_radians(degrees, minutes, seconds, direction):
        """
        Converts degrees, minutes, seconds to decimal degrees
        """
        decimal_degrees = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
        if direction in ['S', 'W']:
            decimal_degrees *= -1
        return math.radians(decimal_degrees)

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

        latitude = cls.degrees_to_radians(lat_degrees, lat_minutes, lat_seconds, lat_direction)
        longitude = cls.degrees_to_radians(lon_degrees, lon_minutes, lon_seconds, lon_direction)

        connections_info = parts[1].split()
        connections = {connections_info[i].replace("va-",""): float(connections_info[i + 1]) for i in range(0, len(connections_info), 2)}
    
        return cls(name, longitude, latitude, connections) 

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: python city_string")
        sys.exit(1)
    string = sys.argv[1]
    city = City.from_string(string)
    print(repr(city))
