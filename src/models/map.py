import sys
from city import City

class Map:
    def __init__(self, cities):
        """
        Initializes a map with cities
        """
        self.cities = cities

    def __str__(self):
        """
        Returns the names of the cities in the map
        """
        return str([str(city) for city in self.cities])

    def __repr__(self):
        """
        Returns a string representation of the map
        """
        return f"Map(cities={self.cities})"

    @staticmethod 
    def map_lines_from_filename(file_name):
        file_path = "../../map_data/" + file_name + ".txt"
        try:
            with open(file_path, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Failed to open {file_path}")
            sys.exit(1)
        lines = [line.strip() for line in lines]
        return lines

    @classmethod
    def from_file(cls, file_name):
        lines = cls.map_lines_from_filename(file_name)
        cities = [City.from_string(line) for line in lines]
        cities_mapped = {city.get_name():city for city in cities}
        return cls(cities_mapped)

if __name__ == "__main__":
    map = Map.from_file("france")
    print(map)
