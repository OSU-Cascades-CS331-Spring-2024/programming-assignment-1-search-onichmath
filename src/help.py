
def usage():
    print("Usage: python main.py -M <map_name> -A <start_city> -B <end_city> -S <search_algorithm>")

def help():
    usage()
    print("Search algorithms: bfs, iddls, ucs, astar")

if __name__ == "__main__":
    help()
