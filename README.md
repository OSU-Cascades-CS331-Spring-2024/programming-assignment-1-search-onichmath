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
 * `BFSAgent`: The Breadth First Search Agent explores the map in a breadth first manner. The agent explored the environment efficiently, expanding a small number of nodes and maintaining the smallest number of nodes in the frontier. However, the agent does not consider cost and thus found the least amount of optimal solutions.
 * `UCSAgent`: The Uniform Cost Search Agent explores the map by expanding the node with the lowest path cost f(n) = g(n). The UCSAgent found the most optimal solutions, showcasing how considering cost leads to optimal results. The agent outperformed A* in the number of optimal solutions by a margin, but explored more of the environment to find these solutions.
 * `IDDLSAgent`: The Iterative Deepening Depth Limited Search Agent explores the map by performing a depth limited search with increasing depth limits starting at 0. The agent explored, expanded, and maintained the most nodes out of all the agents yet found the second fewest optimal solutions. If a heuristic had been utilized to decide the depth limit, the agent would have performed better.
 * `AStarEuclideanAgent`: The A* Euclidean Agent explores the map by expanding the node with the lowest cost f(n) = g(n) + h(n). The heuristic for the Euclidean Agent was the euclidean distance between the considered node and the goal. The euclidean distance was found by converting the latitude and longitude of the nodes to radians and then Cartesian coordinates. The A* Euclidean Agent found the second most optimal solutions, but exhibited efficent exploration due to its heuristic. While the heuristic led to worse performance than UCS, the agent avoided unnecessary exploration and expansion of nodes, focusing on promising paths.
 * `AStarHaversineAgent`: The A* Haversine Agent utilized the Haversine formula to calculate the heuristic cost. The Haversine Agent had equivalent results to the A* Euclidean Agent, suggesting that the distances found by the heuristics were not significantly different.
