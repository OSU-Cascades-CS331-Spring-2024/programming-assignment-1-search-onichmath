from models.map import Map

class Agent:

    total_cost = 0
    total_explored = 0
    total_expanded = 0
    total_maintained = 0
    total_optimal_solutions = 0
    num_runs = 0

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

    def maintain(self):
        """
        Maintains the frontier
        """
        self.maintained += 1
        self.total_maintained += 1

    def explore(self):
        """
        Explores the frontier
        """
        self.explored += 1
        self.total_explored += 1

    def expand(self):
        """
        Expands the frontier
        """
        self.expanded += 1
        self.total_expanded += 1

    def add_optimal_solution(self):
        """
        Adds an optimal solution
        """
        self.total_optimal_solutions += 1

    def add_cost(self, cost):
        """
        Adds the cost to the agent
        """
        self.cost = cost
        self.total_cost += cost

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
        """
        Returns the path as a string
        """
        path_string = ""
        for i in range(len(self.path)):
            if (i == len(self.path) - 1):
                path_string += self.path[i]
                break
            path_string += self.path[i] + " -> "
        return path_string

    def get_path_test_string(self, map:Map):
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

    def get_class_metrics(self):
        """
        Returns the class metrics
        """
        optimal_solutions = self.total_optimal_solutions
        explored = round(self.total_explored / self.num_runs, 2)
        expanded = round(self.total_expanded / self.num_runs, 2)
        maintained = round(self.total_maintained / self.num_runs, 2)
        cost = round(self.total_cost / self.num_runs, 2)
        return f"{self.__class__.__name__}\nOptimal solutions: {optimal_solutions}\nExplored: {explored}\nExpanded: {expanded}\nMaintained: {maintained}\nCost: {cost}\n"

    def add_run(self):
        """
        Adds a run
        """
        self.num_runs += 1
