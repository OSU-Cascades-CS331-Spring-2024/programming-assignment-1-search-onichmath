import heapq
from agents.agent import Agent
from models.node import Node

class UCSAgent(Agent):
    """
    function UNIFORM-COST-SEARCH(problem) returns a solution node, or failure
        return BEST-FIRST-SEARCH(problem, PATH-COST)

    function BEST-FIRST-SEARCH(problem, f) returns a solution node, or failure
        node <- NODE(problem.INITIAL)
        frontier <- a priority queue ordered by f, with node as an element
        reached <- a lookup table, with one entry with key problem.INITIAL and value node

        while not EMPTY(frontier) do
            node <- POP(frontier)
            if problem.IS-GOAL(node.STATE) then return node
            for each child in EXPAND(problem, node) do
                s <- child.STATE
                if s not in reached or child.PATH-COST < reached[s].PATH-COST then
                    reached[s] <- child
                    add child to frontier
        return failure
    """
    def __init__(self):
        super().__init__()

    def search(self, problem):
        """
        Searches the problem for a solution
        """
        # Initialize the frontier with the initial node
        node = Node(problem.start_state, 0, [problem.start_state.name])

        frontier = [[node.path_cost, node]]
        heapq.heapify(frontier)

        reached = {node.state: node}

        while frontier:
            node = heapq.heappop(frontier)[1]
            print(node)

            self.explored += 1
            if problem.goal_test(node.state):
                self.maintained = len(reached)
                self.cost = node.path_cost
                self.path = node.path
                return node 

