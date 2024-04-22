import argparse
from usage import get_maps

class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Argument Parser for Search Algorithms")

        self.parser.add_argument("-A", "-a", help="Start city")

        self.parser.add_argument("-B", "-b", help="End city")


        algorithm_choices = ["bfs", "dfs", "ucs", "dls", "astar"]
        self.parser.add_argument("-S", "-s", choices=algorithm_choices, help=f"Search algorithm to use. Options are: bfs, dfs, ucs, dls, astar")

        map_choices = get_maps()
        self.parser.add_argument("-M", "-m", choices=map_choices, help=f"Map file name w/o extension. Options are {map_choices}")

        heuristic_choices = ["euclidean", "haversine"] 
        self.parser.add_argument("-H", "--heuristic", choices=heuristic_choices, help="Heuristic to use for A* search. Options are: euclidean, haversine")

        self.args = self.parser.parse_args()

    def get_cities(self):
        if self.args.A and self.args.B:
            return [[self.args.A, self.args.B]]
        return [["brest", "nice"],
                ["montpellier", "calais"],
                ["strasbourg", "bordeaux"],
                ["paris", "grenoble"],
                ["grenoble", "paris"],
                ["brest", "grenoble"],
                ["grenoble", "brest"],
                ["nice", "nantes"],
                ["caen", "strasbourg"]]

    def get_algorithm(self):
        if self.args.S:
            return self.args.S 
        return [
            "bfs",
            "ucs",
            "dls",
            "astar"
                ]

    def get_map(self):
        if self.args.M:
            return self.args.M
        return "france"

