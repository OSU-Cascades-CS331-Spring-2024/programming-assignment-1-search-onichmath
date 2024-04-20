import os

def usage():
    print("Usage: python main.py -M <map_name> -A <start_city> -B <end_city> -S <search_algorithm>")

def list_maps():
    maps = os.listdir("../map_data")
    # maps = [map.split(".")[0] for map in maps]
    return maps

def help():
    usage()
    list_maps()
    print("Search algorithms: bfs, iddls, ucs, astar")

if __name__ == "__main__":
    help()
