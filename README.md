# Introduction
This project is part of the Artificial Intelligence class at Oregon State University Cascades. The goal of the project was to implement different search agents and compare their performance on a map of France.
| Agent                | Optimal solutions | Explored | Expanded | Maintained | Cost    |
|----------------------|-------------------|----------|----------|------------|---------|
| BFSAgent             | 2                 | 10.33    | 33.0     | 13.22      | 1135.89 |
| UCSAgent             | 9                 | 15.89    | 49.11    | 18.22      | 1052.78 |
| IDDLSAgent           | 3                 | 146.89   | 148.78   | 153.11     | 1118.78 |
| AStarEuclideanAgent  | 8                 | 9.22     | 29.22    | 15.33      | 1054.78 |
| AStarHaversineAgent  | 8                 | 9.22     | 29.22    | 15.33      | 1054.78 |
# Agents
 * BFSAgent: The Breadth First Search Agent explores the map in a breadth first manner. In the case of the France map, the BFSAgent found the fewest optimal solutions. The agent explored the second fewest nodes and expanded the second fewest nodes. The agent maintained the fewest nodes in the frontier, but its solutions had the highest average cost.
 * UCSAgent: The Uniform Cost Search Agent explores the map by expanding the node with the lowest path cost. The UCSAgent found the most optimal solutions but explored and expanded the second most amount of nodes.
 * IDDLSAgent: The Iterative Deepening Depth Limited Search Agent explores the map by performing a depth limited search with increasing depth limits. The IDDLSAgent found the second fewest optimal solutions. The agent explored, expanded, and maintained the most nodes due to the algorithm restarting the search at each depth limit.
 * AStarEuclideanAgent: The A* Euclidean Agent explores the map by expanding the node with the lowest path cost plus the heuristic cost. The heuristic for the Euclidean Agent was the euclidean distance between the considered node and the goal. The euclidean distance was found by converting the latitude and longitude of the nodes to radians and then Cartesian coordinates. The A* Euclidean Agent found the second most optimal solutions, but explored the fewest number of nodes.
 * AStarHaversineAgent: The A* Haversine Agent utilized the Haversine formula to calculate the heuristic cost. The Haversine Agent had equivalent results to the A* Euclidean Agent implying that the heuristic costs were similar.
# Discussion
Out of the five different agents, the UCSAgent found the most optimal solutions. The A* agent performed similarly while exploring, expanding, and maintaining fewer nodes. This may lead to better performance in larger environments, and A* should be considered over UCS in most cases due to this improvement.
