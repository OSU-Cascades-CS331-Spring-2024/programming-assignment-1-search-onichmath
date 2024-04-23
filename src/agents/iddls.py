from agents.agent import Agent
from models.node import Node
from models.problem import Problem

class IDDLSAgent(Agent):
    """
    Iterative Deepening Depth-Limited Search Agent
    The following pseudocode is from Artificial Intelligence: A Modern Approach page 182

    function ITERATIVE-DEEPENING-SEARCH(problem) returns a solution node or failure
        for depth = 0 to infinity do
            result <- DEPTH-LIMITED-SEARCH(problem, depth)
            if result != cutoff then return result

    function DEPTH-LIMITED-SEARCH(problem, limit) returns a solution node, failure, or cutoff
        frontier <- a LIFO queue (stack), with NODE(problem.INITIAL) as an element
        reached <- failure
        while not IS-EMPTY(frontier) do
            node <- POP(frontier)
            if problem.IS-GOAL(node.STATE) then return node
            if DEPTH(node) > limit then
                result <- cutoff
            else if not IS-CYCLE(node) then
                for each child in EXPAND(problem, node) do
                    add child to frontier
        return result

    """

    def __init__(self):
        """
        Initializes the agent
        """
        super().__init__()

    def generate_infinite_numbers(self):
        """
        Generates an infinite sequence of numbers
        """
        i = 0
        while True:
            yield i
            i += 1

    def depth_limited_search(self, problem:Problem, limit):
        """
        Searches the problem for a solution using depth-limited search
        Frontier is a LIFO queue (stack)
        """
        frontier = [Node(problem.start_state, 0, [problem.start_state.name])]
        result = "failure"
        self.maintain()

        while frontier:
            node = frontier.pop(-1)
            self.explore()

            if problem.goal_test(node.state):
                self.add_cost(node.path_cost)
                self.path = node.path
                return node 

            if node.depth() > limit:
                result = "cutoff"

            elif not node.is_cycle():
                for child in problem.expand(node):
                    self.expand()
                    frontier.append(child)
                    self.maintain()

        return result


    def search(self, problem:Problem):
        """
        Searches the problem for a solution using iterative deepening depth-limited search
        Iterative deepening depth-limited search uses depth-limited search with increasing depths
        """
        self.add_run()
        for depth in self.generate_infinite_numbers():
            result = self.depth_limited_search(problem, depth)
            if result != "cutoff":
                return result
