# Lecture 5.3 - Single Source Shortest Paths with Negative Weights (Bellman-Ford Algorithm)_annotated.pdf (PDF file)
**Summary**
## Single Source Shortest Paths with Negative Weights

### Dijkstra's Algorithm

Dijkstra's algorithm works by iteratively discovering the shortest paths from the source vertex to all other vertices in the graph. It maintains a set of vertices that have been visited and a set of vertices that have not yet been visited. At each iteration, it chooses the unvisited vertex with the smallest distance from the source vertex and adds it to the visited set. It then updates the distances to all of the neighbors of the newly visited vertex.

Dijkstra's algorithm requires that all edge weights be non-negative. If there are negative edge weights, then the algorithm may not find the shortest path.

### Bellman-Ford Algorithm

The Bellman-Ford algorithm is a generalization of Dijkstra's algorithm that can handle negative edge weights. It works by iteratively relaxing all of the edges in the graph. Relaxation means updating the distance to a vertex to be the minimum of its current distance and the distance to the vertex plus the weight of the edge.

The Bellman-Ford algorithm terminates after n iterations, where n is the number of vertices in the graph. If there are no negative cycles in the graph, then the algorithm will find the shortest path from the source vertex to all other vertices. If there is a negative cycle, then the algorithm will not terminate and will continue to relax the edges indefinitely.

### Complexity

The Bellman-Ford algorithm has a time complexity of O(mn), where m is the number of edges in the graph and n is the number of vertices. This is slower than Dijkstra's algorithm, which has a time complexity of O(n^2). However, the Bellman-Ford algorithm can handle negative edge weights, while Dijkstra's algorithm cannot.

### Applications

The Bellman-Ford algorithm is used in a variety of applications, including:

* Finding the shortest path between two vertices in a graph with negative edge weights
* Finding the minimum cost cycle in a graph
* Finding the minimum cost flow in a network

### Example

Consider the following graph:

```
0 -> 1: 1
0 -> 2: 2
1 -> 2: -1
2 -> 0: -2
2 -> 3: 1
3 -> 2: -1
```

The Bellman-Ford algorithm would start by initializing the distance to all vertices to infinity, except for the source vertex, which would be set to 0. It would then relax all of the edges in the graph.

After the first iteration, the distances to vertices 1, 2, and 3 would be:

```
0 -> 1: 1
0 -> 2: 2
1 -> 2: 0
2 -> 0: -2
2 -> 3: 1
3 -> 2: 0
```

After the second iteration, the distances to vertices 2 and 3 would be:

```
0 -> 1: 1
0 -> 2: 2
1 -> 2: 0
2 -> 0: -2
2 -> 3: 0
3 -> 2: 0
```

After the third iteration, the distances to vertices 3 and 2 would be:

```
0 -> 1: 1
0 -> 2: 2
1 -> 2: 0
2 -> 0: -2
2 -> 3: 0
3 -> 2: 0
```

The algorithm would then terminate, since there are no more edges to relax. The final distances to the vertices would be:

```
0 -> 1: 1
0 -> 2: 2
1 -> 2: 0
2 -> 0: -2
2 -> 3: 0
3 -> 2: 0
```

### Implementation

The following Python code implements the Bellman-Ford algorithm:

```python
def bellman_ford(graph, source):
  """
  Finds the shortest path from a source vertex to all other vertices in a graph with negative edge weights.

  Args:
    graph: A dictionary representing the graph. The keys are the vertices and the values are dictionaries representing the edges.
    source: The source vertex.

  Returns:
    A dictionary representing the distances from the source vertex to all other vertices.
  """

  # Initialize the distances to all vertices to infinity.
  distances = {}
  for vertex in graph:
    distances[vertex] = float('inf')

  # Set the distance to the source vertex to 0.
  distances[source] = 0

  # Relax all of the edges in the graph n times.
  for i in range(len(graph)):
    for vertex in graph:
      for neighbor, weight in graph[vertex].items():
        if distances[vertex] + weight < distances[neighbor]:
          distances[neighbor] = distances[vertex] + weight

  # Check if there is a negative cycle.
  for vertex in graph:
    for neighbor, weight in graph[vertex].items():
      if distances[vertex] + weight < distances[neighbor]:
        raise ValueError("There is a negative cycle in the graph.")

  # Return the distances.
  return distances
```

### Conclusion

The Bellman-Ford algorithm is a powerful algorithm for finding the shortest path from a source vertex to all other vertices in a graph with negative edge weights. It is more complex than Dijkstra's algorithm, but it can handle a wider range of graphs.
