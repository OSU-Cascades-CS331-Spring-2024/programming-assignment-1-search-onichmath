class Node:
    def __init__(self, state, path_cost, path):
        """
        Initializes a node with a state and parent
        """
        self.state = state
        self.path_cost = path_cost
        self.path = path 

    def __str__(self):
        """
        Returns the state of the node
        """
        return f"{self.state.name}, {self.path_cost}, {self.path}"
