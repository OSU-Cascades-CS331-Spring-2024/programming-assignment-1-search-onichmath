from agents.agent import Agent
from models.node import Node

class BFSAgent(Agent):
    """
    Breadth-First Search Agent
    The following pseudocode is from Artificial Intelligence: A Modern Approach page 176

    function BREADTH-FIRST-SEARCH(problem) returns a solution node or failure
        node <- NODE(problem.INITIAL)

        if problem.IS-GOAL(node.STATE) then return node

        frontier <- a FIFO queue, with node as an element
        reached <- {problem.INITIAL}

        while not EMPTY(frontier) do
            node <- POP(frontier)

            for each child in EXPAND(problem, node) do
                s <- child.STATE
                if problem.IS-GOAL(s) then return child
                if s not in reached then
                    add s to reached
                    add child to frontier

        return failure
    """

    def __init__(self):
        """
        Initializes the agent
        """
        super().__init__()

    def search(self, problem):
        """
        Searches the problem for a solution using breadth-first search
        Breadth-first search uses a FIFO queue to explore
        """
        # Initialize the frontier with the initial node
        node = Node(problem.start_state, 0, [problem.start_state.name])

        if problem.goal_test(node.state):
            return node

        frontier = [node]

        reached = set([node.state])

        while frontier:
            node = frontier.pop(0)

            self.explored += 1

            for child in problem.expand(node):
                self.expanded += 1

                if problem.goal_test(child.state):
                    self.maintained = len(reached)
                    self.cost = child.path_cost
                    self.path = child.path
                    return child

                if child.state not in reached:
                    reached.add(child.state)
                    frontier.append(child)
        return None
