from models.city import City
from models.node import Node

class Problem():
    def __init__(self, start_city_name, goal_city_name, map):
        """
        Initializes a problem with a start and goal state
        """
        self.start_state = start_city_name
        self.goal_state = goal_city_name
        self.map = map

    def __str__(self):
        return f"Problem: {self.start_state} -> {self.goal_state}"

    def actions(self, state):
        """
        Returns the possible actions from the given state
        """
        return state.get_connections()

    def goal_test(self, state):
        """
        Returns whether the given state is the goal state
        """
        return state == self.goal_state

    def result(self, state, action):
        """
        Returns the state that results from the given action
        """
        return action

    def action_cost(self, state, state_prime):
        """
        Returns the cost of the given action
        """
        return state.get_cost(state_prime.name)

    def expand(self, node):
        """
        Expands the given node
        """
        s = node.state
        for action in self.actions(s):
            s_prime = self.map.get_city(self.result(s, action))
            c = node.path_cost + self.action_cost(s, s_prime)
            yield Node(s_prime, c, node.path + [s_prime.name])
