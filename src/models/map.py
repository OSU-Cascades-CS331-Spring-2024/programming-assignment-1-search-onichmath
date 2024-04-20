class Map:
    def __init__(self, cities):
        """
        Initializes a map with cities
        """
        self.cities = cities

    @classmethod
    def from_file(cls, file_name):
        file_path = "../../map_data/" + file_name + ".txt"
        with open(file_path, "r") as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]
        print(lines)

if __name__ == "__main__":
    Map.from_file("france")
