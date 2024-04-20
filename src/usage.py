import os

def usage():
    print("Usage: python main.py -M <map_name> -A <start_city> -B <end_city> -S <search_algorithm>")

def get_maps():
    maps = os.listdir("../map_data")
    # maps = [map.split(".")[0] for map in maps]
    return maps

def list_maps_and_cities():
    maps = get_maps()
    print()
    print(f"Available maps and cities:")
    for map in maps:
        cities = []
        with open(f"../map_data/{map}", "r") as f:
            lines = f.readlines()
            for line in lines:
                city = line.split(" ")[0]
                cities.append(city)
        print(f"Map: {map.split('.')[0]}")
        print("Cities:")
        for i in range(0, len(cities), 5):
            print(f"{' '.join(cities[i:i+5])}")
    print()


def help():
    usage()
    list_maps_and_cities()
    print("Search algorithms: bfs, iddls, ucs, astar")

if __name__ == "__main__":
    help()
