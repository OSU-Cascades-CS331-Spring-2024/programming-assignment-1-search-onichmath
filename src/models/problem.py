from models.city import City
from math import cos, sin,  sqrt, radians, asin
from models.node import Node

class Problem():
    polar_earth_radius_km = 6357.0

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

    def heuristic_euclidean(self, state):
        """
        Returns the heuristic value for the given state using euclidean distance
        """
        x1, y1, z1 = self.polar_to_cartesian_km(state.longitude, state.latitude)
        x2, y2, z2 = self.polar_to_cartesian_km(self.goal_state.longitude, self.goal_state.latitude)
        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5

        return d

    def heuristic_haversine(self, state):
        """
        Returns the heuristic value for the given state using haversine's formula
        https://en.wikipedia.org/wiki/Haversine_formula
        """
        phi_1, phi_2 = state.latitude, self.goal_state.latitude
        lambda_1, lambda_2 = state.longitude, self.goal_state.longitude
        dphi = phi_2 - phi_1
        dlambda = lambda_2 - lambda_1

        h = (1 - cos(dphi) + cos(phi_1) * cos(phi_2) * (1 - cos(dlambda))) / 2
        d = 2 * self.polar_earth_radius_km * asin(sqrt(h))

        return d

    def polar_to_cartesian_km(self, longitude, latitude):
        """
        Converts spherical polar coordinates to cartesian coordinates, assuming the Earth is a sphere
        https://stackoverflow.com/questions/1185408/converting-from-longitude-latitude-to-cartesian-coordinates
        """
        x = cos(latitude) * cos(longitude) * self.polar_earth_radius_km
        y = cos(latitude) * sin(longitude) * self.polar_earth_radius_km
        z = sin(latitude) * self.polar_earth_radius_km
        return x, y, z
