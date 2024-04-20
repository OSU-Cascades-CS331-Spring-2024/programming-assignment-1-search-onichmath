import usage
import sys
from agents.bfs import BFSAgent
from models.problem import Problem
from models.map import Map
from models.city import City


if __name__ == "__main__":
    map = Map.from_file("france")
    start_city = map.cities["brest"]
    goal_city = map.cities["nice"]
    problem = Problem(start_city, goal_city, map)
    agent = BFSAgent()
    solution = agent.search(problem)
    print(agent)
