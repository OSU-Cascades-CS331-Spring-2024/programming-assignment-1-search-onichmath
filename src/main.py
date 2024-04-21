import usage
import sys
from agents.bfs import BFSAgent
from agents.ucs import UCSAgent
from agents.iddls import IDDLSAgent
from models.problem import Problem
from models.map import Map


if __name__ == "__main__":
    map = Map.from_file("france")
    start_city = map.cities["brest"]
    goal_city = map.cities["nice"]
    problem = Problem(start_city, goal_city, map)

    ucs_agent = UCSAgent()
    bfs_agent = BFSAgent()
    iddls_agent = IDDLSAgent()

    ucs_solution = ucs_agent.search(problem)
    bfs_solution = bfs_agent.search(problem)
    iddls_solution = iddls_agent.search(problem)


    print(f"{problem}\n")
    print(f"{bfs_agent}\n")
    print(f"{ucs_agent}\n")
    print(f"{iddls_agent}\n")
