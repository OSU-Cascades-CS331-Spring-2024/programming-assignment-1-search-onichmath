from models.city import City
class Node:
    def __init__(self, state:City, path_cost, path):
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

    def is_cycle(self):
        """
        Returns whether the node is a cycle
        """
        return self.state.name in self.path[:-1]

    def depth(self):
        """
        Returns the depth of the node
        """
        return len(self.path) - 1
