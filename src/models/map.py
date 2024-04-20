import sys

class Map:
    def __init__(self, cities):
        """
        Initializes a map with cities
        """
        self.cities = cities

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
        pass

if __name__ == "__main__":
    Map.from_file("france")
