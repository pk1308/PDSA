# Lecture 4.4 - Depth First Search (DFS)_T.pdf (PDF file)
**Summary**
Depth First Search (DFS) is an alternative search strategy to BFS, using a stack instead of a queue. In DFS, we start from a vertex, explore an unexplored neighbor, then explore that neighbor's unexplored neighbors, and so on, following a path until we reach a vertex with no unexplored neighbors. We then backtrack, systematically revisiting previous vertices to explore any unexplored neighbors they may have.

Unlike BFS, where we explore all neighbors of the first level, then all neighbors of the second level, DFS explores paths in a depth-first manner. This allows us to explore more deeply into the graph, but also means we may not find the shortest path to a destination.

In order to keep track of which vertices have been visited and which vertex led to their discovery (parent), DFS uses a stack, implemented either explicitly or implicitly through recursion. When using recursion, visited and parent are global variables, which DFS updates as it explores.

In terms of complexity, DFS has a time complexity similar to BFS. Exploring each vertex requires linear time, as does checking for unexplored neighbors. Thus, with an adjacency matrix, the worst-case complexity is O(n^2), and with an adjacency list, it is O(m + n).

While DFS does not provide information about shortest paths like BFS, it is often more informative about the graph structure, making it a valuable tool for exploring graphs and understanding their connectivity.
**Lec file**
# Lecture 4.4 - Depth First Search (DFS)_T.pdf (PDF file)
![Alt text](<./Lecture 4.4 - Depth First Search (DFS)_T.pdf>){ type=application/pdf style="min-height:100vh;width:100%" }