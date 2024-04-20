class Agent:
    def __init__(self):
        """
        Initializes an agent with a path, cost, and metrics
        Metrics:
        - Explored: Average number of nodes removed from frontier
        - Expanded: Average number of nodes added to frontier
        - Maintained: Average number of nodes stored in the frontier
        """
        # Path
        self.current_path = [] 
        self.current_cost = 0 
        # Metrics
        self.explored = 0 
        self.expanded = 0 
        self.maintained = 0

    def reset_agent(self):
        """
        Resets the agent's path, cost, and metrics
        """
        self.current_path = [] 
        self.current_cost = 0 
        self.explored = 0 
        self.expanded = 0 
        self.maintained = 0

    def __str__(self):
        """
        Returns the agent's  metrics
        """
        return f"Path: {self.current_path}\nCost: {self.current_cost}\nExplored: {self.explored}\nExpanded: {self.expanded}\nMaintained: {self.maintained}"
