class Problem():
    def __init__(self, start_city_name, goal_city_name, map):
        """
        Initializes a problem with a start and goal state
        """
        self.start_state = start_city_name
        self.goal_state = goal_city_name
        self.map = map

    def actions(self, state):
        """
        Returns the possible actions from the given state
        """
        return state.get_connections()

    def goal_test(self, state):
        """
        Returns whether the given state is the goal state
        """
        return state.name == self.goal_state

    def result(self, state, action):
        """
        Returns the state that results from the given action
        """
        return action

    def action_cost(self, state, state_prime):
        """
        Returns the cost of the given action
        """
        return state.get_cost(state_prime)
