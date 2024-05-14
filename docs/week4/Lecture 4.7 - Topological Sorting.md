# Lecture 4.7 - Topological Sorting.pdf (PDF file)
**Summary**
Topological sorting is a technique used to organize a set of tasks or activities with dependencies into a sequence that respects those dependencies. It is particularly useful in situations where tasks must be completed in a specific order to avoid conflicts or errors.

Key concepts in topological sorting include:

1. Directed Acyclic Graphs (DAGs): Topological sorting is applicable to directed acyclic graphs (DAGs), which are graphs that contain no cycles, meaning there is no path from any vertex back to itself.

2. Indegree: Indegree refers to the number of incoming edges into a vertex in a directed graph.

3. Topological Sort: A topological sort is a linear arrangement of vertices in a graph that preserves the dependencies between the vertices.

4. Algorithm: The topological sorting algorithm works by iteratively identifying vertices with an indegree of 0 and removing them from the graph. The removed vertices are placed in the topological order. This process is repeated until all vertices have been listed.

5. Complexity: The complexity of the topological sorting algorithm using an adjacency matrix is O(n^2), where n represents the number of vertices in the graph. However, using an adjacency list, the complexity can be reduced to O(m + n), where m represents the number of edges in the graph.
**Lec file**
# Lecture 4.7 - Topological Sorting.pdf (PDF file)
![Alt text](<./Lecture 4.7 - Topological Sorting.pdf>){ type=application/pdf style="min-height:100vh;width:100%" }