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
    algorithm = parser.get_algorithm()
    agents = [BFSAgent(), UCSAgent(), IDDLSAgent(), AStarEuclideanAgent(), AStarHaversineAgent()]
    print(parser.get_map())

    map = Map.from_file(parser.get_map())

    for city_pair in cities:
        start_city = map.cities[city_pair[0]]
        goal_city = map.cities[city_pair[1]]
        problem = Problem(start_city, goal_city, map)
        print(f"{problem}\n")
        costs = []
        for agent in agents:
            solution = agent.search(problem)
            costs.append(solution.path_cost)
            print(f"{agent}\n")
            agent.reset_agent()
        min_cost = min(costs)
        min_indices = [i for i, x in enumerate(costs) if x == min_cost]
        for i in min_indices:
            agents[i].add_optimal_solution()
    for agent in agents:
        print(f"{agent.get_class_metrics()}\n")


def run_algorithm(parser):
    algorithm = parser.get_algorithm()
    map = Map.from_file(parser.get_map())
    cities = parser.get_cities_names()
    start_city = map.cities[cities[0][0]]
    goal_city = map.cities[cities[0][1]]
    problem = Problem(start_city, goal_city, map)

    if algorithm == "bfs":
        bfs_agent = BFSAgent()
        solution = bfs_agent.search(problem)
        print(f"{bfs_agent}\n")
    elif algorithm == "ucs":
        ucs_agent = UCSAgent()
        solution = ucs_agent.search(problem)
        print(f"{ucs_agent}\n")
    elif algorithm == "iddls":
        iddls_agent = IDDLSAgent()
        solution = iddls_agent.search(problem)
        print(f"{iddls_agent}\n")
    elif algorithm == "astar":
        heuristic = parser.get_heuristic()
        for h in heuristic:
            astar_agent = AStarAgent(heuristic=h)
            solution = astar_agent.search(problem)
            print(f"{astar_agent}\n")
            astar_agent.reset_agent()
    else:
        usage.help()


def main():
    parser = ArgParser()
    if parser.no_cities():
        run_all_algorithms(parser)
    else:
        run_algorithm(parser)







if __name__ == "__main__":
    main()
    # parser = ArgParser()
    # map = Map.from_file("france")
    # start_city = map.cities["brest"]
    # goal_city = map.cities["nice"]
    # problem = Problem(start_city, goal_city, map)
    #
    # ucs_agent = UCSAgent()
    # bfs_agent = BFSAgent()
    # iddls_agent = IDDLSAgent()
    # astar_agent = AStarAgent()
    #
    # ucs_solution = ucs_agent.search(problem)
    # bfs_solution = bfs_agent.search(problem)
    # iddls_solution = iddls_agent.search(problem)
    #
    # astar_euclidean_solution = astar_agent.search(problem, heuristic="euclidean")
    # print(f"{astar_agent}\n")
    # astar_agent.reset_agent()
    # astar_haversine_solution = astar_agent.search(problem, heuristic="haversine")
    # print(f"{astar_agent}\n")
    #
    #
    # print(f"{problem}\n")
    # print(f"{bfs_agent}\n")
    # print(f"{ucs_agent}\n")
    # print(f"{iddls_agent}\n")
