class Agent:
    def __init__(self, start, goal, map):
        """
        Initializes an agent with a start, goal, and map
        The agent also has a path, cost, and metrics
        Metrics:
        - Explored: Average number of nodes removed from frontier
        - Expanded: Average number of nodes added to frontier
        - Maintained: Average number of nodes stored in the frontier
        """
        # Start, goal, and map
        self.start = start 
        self.goal = goal
        self.map = map
        # Path
        self.path = [] 
        self.cost = 0 
        # Metrics
        self.explored = 0 
        self.expanded = 0 
        self.maintained = 0
