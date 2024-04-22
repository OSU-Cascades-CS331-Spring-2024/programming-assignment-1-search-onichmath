import argparse
from usage import get_maps

class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Argument Parser for Search Algorithms")

        self.parser.add_argument("-A", "-a", help="Start city")

        self.parser.add_argument("-B", "-b", help="End city")


        algorithm_choices = ["bfs", "dfs", "ucs", "iddls", "astar"]
        self.parser.add_argument("-S", "-s", choices=algorithm_choices, help=f"Search algorithm to use. Options are: bfs, dfs, ucs, iddls, astar")

        map_choices = get_maps()
        self.parser.add_argument("-M", "-m", choices=map_choices, help=f"Map file name w/o extension. Options are {map_choices}")

        heuristic_choices = ["euclidean", "haversine"] 
        self.parser.add_argument("-H", "--heuristic", choices=heuristic_choices, help="Heuristic to use for A* search. Options are: euclidean, haversine")


    def parse_args(self, args=None):
        return self.parser.parse_args(args)
