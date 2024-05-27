# Lecture 5.3 - Single Source Shortest Paths with Negative Weights (Bellman-Ford Algorithm)_annotated.pdf (PDF file)
**Summary**
The Bellman-Ford algorithm is used to find the shortest paths from a single source vertex to all other vertices in a weighted graph that may contain negative edge weights. Unlike Dijkstra's algorithm, which assumes non-negative edge weights, the Bellman-Ford algorithm allows for negative weights.

Initially, the distance to all vertices is set to infinity except for the source vertex, which is set to 0. The algorithm then iteratively updates the distance to each vertex by considering all the edges that connect it to its neighbors. After n iterations (where n is the number of vertices in the graph), the algorithm converges and the resulting distance values represent the shortest paths from the source to all other vertices.

The Bellman-Ford algorithm takes O(nm) time, where n is the number of vertices in the graph and m is the number of edges. If the graph contains negative cycles, the algorithm will detect them and report that no shortest path exists.
**Lec file**
# Lecture 5.3 - Single Source Shortest Paths with Negative Weights (Bellman-Ford Algorithm)_annotated.pdf (PDF file)
![Alt text](<./Lecture 5.3 - Single Source Shortest Paths with Negative Weights (Bellman-Ford Algorithm)_annotated.pdf>){ type=application/pdf style="min-height:100vh;width:100%" }