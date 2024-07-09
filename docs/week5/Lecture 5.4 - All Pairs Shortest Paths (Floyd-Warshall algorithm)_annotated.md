# Lecture 5.4 - All Pairs Shortest Paths (Floyd-Warshall algorithm)_annotated.pdf (PDF file)
**Summary**
## All-Pairs Shortest Paths

**Introduction:**

In weighted graphs, finding the shortest paths between every pair of vertices is a fundamental problem with applications in various domains, such as network routing, logistics, and social network analysis. This problem is known as the all-pairs shortest path problem.

**Single-Source Shortest Paths vs. All-Pairs Shortest Paths:**

Traditional shortest path algorithms like Dijkstra's algorithm and Bellman-Ford algorithm find the shortest paths from a single source vertex to all other vertices in a graph. In contrast, all-pairs shortest path algorithms determine the shortest paths between every pair of vertices in the graph.

**Transitive Closure:**

An alternative approach to finding all-pairs shortest paths is through the concept of transitive closure. The transitive closure of a graph is a matrix B, where B[i, j] = 1 if there is a path from vertex i to vertex j using any intermediate vertices.

**Warshall's Algorithm:**

Warshall's algorithm is a dynamic programming algorithm that computes the transitive closure of a graph. It iteratively updates the matrix B, starting with direct edges and considering longer paths through intermediate vertices.

**Floyd-Warshall Algorithm:**

The Floyd-Warshall algorithm is an adaptation of Warshall's algorithm for finding all-pairs shortest paths in weighted graphs. It maintains a matrix SP, where SP[i, j, k] represents the shortest path from vertex i to vertex j using vertices in the set {0, 1, ..., k-1} as intermediate vertices.

**Algorithm Steps:**

1. Initialize SP[i, j, 0] to the weight of the direct edge (i, j), or infinity if there is no direct edge.
2. For each intermediate vertex k, iterate over all pairs of vertices i and j.
3. If the path from i to j through k is shorter than the current shortest path from i to j, update SP[i, j, k].
4. After considering all intermediate vertices, SP[i, j, n] contains the shortest path from i to j.

**Implementation:**

The Floyd-Warshall algorithm can be implemented using a straightforward nested loop. However, optimizing space usage is possible by maintaining only two "slices" of the SP matrix and reusing them for the next iteration.

**Time and Space Complexity:**

The time complexity of the Floyd-Warshall algorithm is O(n^3), where n is the number of vertices in the graph. The space complexity can be reduced to O(n^2) by reusing the SP matrix slices.

**Applications:**

The Floyd-Warshall algorithm has numerous applications, including:

* Finding optimal routes in transportation networks
* Computing distances between cities in a map
* Detecting negative cycles in a graph
* Solving the all-pairs maximum flow problem

**Summary:**

The Floyd-Warshall algorithm is an efficient and versatile algorithm for finding all-pairs shortest paths in weighted graphs. It works for both positive and negative edge weights, assuming no negative cycles. The algorithm's time complexity is O(n^3), but space usage can be optimized to O(n^2). Its simplicity and wide range of applications make it a valuable tool in various domains.
