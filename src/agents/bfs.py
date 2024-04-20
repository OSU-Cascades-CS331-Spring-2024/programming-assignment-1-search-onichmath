from agent import Agent

class PseudoQueue:
    """
    A FIFO queue
    """
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

class BFS(Agent):
    """
    Breadth-First Search Agent
    The following pseudocode is from Artificial Intelligence: A Modern Approach

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

    def search(self, problem):
        """
        Searches the problem for a solution
        """
        # Initialize the frontier with the initial node
        node = problem.start_state 

        if problem.goal_test(node):
            return node

        frontier = [node]
        
        while frontier:
            node = frontier.pop(0)

