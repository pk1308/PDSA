# Lecture 5.1 - Shortest Paths in Weighted Graphs_annotated.pdf (PDF file)
**Summary**
**Introduction to Weighted Graphs**

Weighted graphs extend the concept of unweighted graphs by assigning a weight or cost to each edge. This weight can represent various metrics such as distance, time, cost, etc. By considering edge weights, we can compute shortest paths that minimize the total cost or distance traveled.

**Single Source Shortest Paths**

One of the fundamental problems in weighted graphs is finding the shortest paths from a single source vertex to all other vertices. This problem arises in various applications, such as finding the shortest route on a road network or delivering goods from a distribution center to multiple locations.

**Dijkstra's Algorithm**

Dijkstra's algorithm is a widely used method for solving the single source shortest path problem. It maintains a set of vertices whose shortest paths from the source have been determined and iteratively updates its estimate of the shortest paths until it reaches all vertices.

**Implementation of Dijkstra's Algorithm**

The following steps describe the implementation of Dijkstra's algorithm:

1. Initialize a distance array that stores the shortest distance from the source vertex to all other vertices. Initially, all distances are set to infinity except the distance to the source, which is set to 0.
2. While there are still unvisited vertices:
    - Find the unvisited vertex with the smallest distance. This is the current vertex.
    - For each neighbor of the current vertex:
        - Calculate the new distance to the neighbor via the current vertex.
        - If this new distance is shorter than the current shortest distance to the neighbor, update the neighbor's distance and set its predecessor to the current vertex.
3. Once all vertices have been visited, the distance array contains the shortest distances from the source to all other vertices.

**All Pairs Shortest Paths**

In some scenarios, we may need to compute the shortest paths between every pair of vertices in a graph. This problem is known as the all pairs shortest paths problem.

**Floyd-Warshall Algorithm**

The Floyd-Warshall algorithm is a widely used method for solving the all pairs shortest paths problem. It works by iteratively updating a distance matrix to store the shortest paths between all pairs of vertices.

**Implementation of Floyd-Warshall Algorithm**

The following steps describe the implementation of the Floyd-Warshall algorithm:

1. Initialize a distance matrix that stores the shortest distance between all pairs of vertices. Initially, the distances are set to infinity, except for the distances between vertices and themselves, which are set to 0.
2. For each possible intermediate vertex k:
    - For each pair of vertices i and j:
        - Calculate the new distance from i to j through k. This is the minimum of the current shortest distance from i to j and the sum of the shortest distances from i to k and from k to j.
        - If the new distance is shorter than the current shortest distance from i to j, update the shortest distance and set the intermediate vertex to k.
3. Once all intermediate vertices have been considered, the distance matrix contains the shortest distances between all pairs of vertices.

**Negative Edge Weights**

Negative edge weights introduce additional complexity to shortest path problems. Graphs with negative edge weights may contain negative cycles, which can lead to undefined shortest paths.

**Bellman-Ford Algorithm**

The Bellman-Ford algorithm is a modification of Dijkstra's algorithm that can handle negative edge weights. It iteratively updates its estimate of the shortest paths, allowing it to detect negative cycles. However, the Bellman-Ford algorithm is not as efficient as Dijkstra's algorithm for graphs without negative cycles.

**Applications of Shortest Path Algorithms**

Shortest path algorithms have numerous applications in various domains, including:

* **Network routing:** Finding the shortest path between routers or network devices.
* **Transportation planning:** Optimizing routes for vehicles, such as finding the shortest route from a warehouse to multiple delivery locations.
* **Supply chain management:** Determining the most efficient way to transport goods from suppliers to customers.
* **Data analysis:** Identifying the shortest paths in a network to analyze data flow or detect anomalies.
* **Social network analysis:** Finding the shortest paths between individuals or groups in social networks to measure influence or identify connections.
