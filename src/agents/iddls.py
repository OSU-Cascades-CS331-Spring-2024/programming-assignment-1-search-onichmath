from agents.agent import Agent
from models.node import Node

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

