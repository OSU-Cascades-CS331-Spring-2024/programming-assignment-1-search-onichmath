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
        self.path = [] 
        self.cost = 0 
        # Metrics
        self.explored = 0 
        self.expanded = 0 
        self.maintained = 0

    def reset_agent(self):
        """
        Resets the agent's path, cost, and metrics
        """
        self.path = [] 
        self.cost = 0 
        self.explored = 0 
        self.expanded = 0 
        self.maintained = 0

    def get_path_string(self):
        path_string = ""
        for i in range(len(self.path)):
            if (i == len(self.path) - 1):
                path_string += self.path[i]
                break
            path_string += self.path[i] + " -> "
        return path_string

    def get_path_test_string(self, map):
        """
        Tests the path cost
        """
        cost = 0
        for i in range(len(self.path) - 1):
            cost += map.get_cost(self.path[i], self.path[i + 1])
        try:
            assert cost == self.cost
            return f"Path cost: {self.cost} == {cost}"
        except AssertionError:
            return f"Path cost: {self.cost} != {cost}"

    def __str__(self):
        """
        Returns the agent's  metrics
        """
        return f"{self.__class__.__name__}\nPath: {self.get_path_string()}\nCost: {self.cost}\nExplored: {self.explored}\nExpanded: {self.expanded}\nMaintained: {self.maintained}\n"
