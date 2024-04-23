import usage
import sys
from parser import ArgParser
from agents.bfs import BFSAgent
from agents.ucs import UCSAgent
from agents.astar import AStarEuclideanAgent, AStarHaversineAgent
from agents.iddls import IDDLSAgent
from models.problem import Problem
from models.map import Map


def run_all_algorithms(parser):
    cities = parser.get_cities_names()
    agents = [BFSAgent(), UCSAgent(), IDDLSAgent(), AStarEuclideanAgent(), AStarHaversineAgent()]
    map = Map.from_file(parser.get_map())

    with open("../outputs/solutions.txt", "w") as f:
        for city_pair in cities:
            start_city = map.cities[city_pair[0]]
            goal_city = map.cities[city_pair[1]]
            problem = Problem(start_city, goal_city, map)
            f.write(f"{problem}\n")
            costs = []
            for agent in agents:
                solution = agent.search(problem)
                costs.append(solution.path_cost)
                f.write(f"{agent}\n")
                agent.reset_agent()
            min_cost = min(costs)
            min_indices = [i for i, x in enumerate(costs) if x == min_cost]
            for i in min_indices:
                agents[i].add_optimal_solution()
    with open("../README.md", "w") as f:
        for agent in agents:
            f.write(f"{agent.get_class_metrics()}\n")


def run_algorithm(parser):
    try:
        algorithm = parser.get_algorithms()[0]
        map = Map.from_file(parser.get_map())
        cities = parser.get_cities_names()
        start_city = map.cities[cities[0][0]]
        goal_city = map.cities[cities[0][1]]
        problem = Problem(start_city, goal_city, map)

        if algorithm == "bfs":
            bfs_agent = BFSAgent()
            bfs_agent.search(problem)
            print(f"{bfs_agent}\n")
        elif algorithm == "ucs":
            ucs_agent = UCSAgent()
            ucs_agent.search(problem)
            print(f"{ucs_agent}\n")
        elif algorithm == "iddls":
            iddls_agent = IDDLSAgent()
            iddls_agent.search(problem)
            print(f"{iddls_agent}\n")
        elif algorithm == "astar":
            heuristic = parser.get_heuristic()
            if heuristic == ["euclidean"]:
                astar_agent = AStarEuclideanAgent()
                astar_agent.search(problem)
                print(f"{astar_agent}\n")
            elif heuristic == ["haversine"]:
                astar_agent = AStarHaversineAgent()
                astar_agent.search(problem)
                print(f"{astar_agent}\n")
            else:
                astar_agent = AStarEuclideanAgent()
                astar_agent.search(problem)
                print(f"{astar_agent}\n")
                astar_agent.reset_agent()
                astar_agent = AStarHaversineAgent()
                astar_agent.search(problem)
                print(f"{astar_agent}\n")
                astar_agent.reset_agent()
        else:
            raise ValueError("Invalid algorithm")
    except Exception as e:
        print(e)
        usage.help()

def main():
    parser = ArgParser()
    if parser.no_cities():
        run_all_algorithms(parser)
    else:
        run_algorithm(parser)

if __name__ == "__main__":
    main()
