# Lecture 4.4 - Depth First Search (DFS)_.pdf (PDF file)
**Summary**
Depth First Search (DFS) is a technique in graph theory to explore graphs systematically. In DFS, we start from a vertex, visit an unexplored neighbor, and continue exploring its neighbors until all neighbors are visited. If there are still unexplored neighbors, we backtrack to the nearest suspended vertex that still has an unexplored neighbor.

DFS is often implemented using a stack. This is because we need to keep track of the vertices we have visited but not yet fully explored. As we visit a vertex, we push it onto the stack. When we have explored all of its neighbors, we pop it from the stack.

The complexity of DFS is O(n^2) using an adjacency matrix and O(m + n) using an adjacency list, where n is the number of vertices and m is the number of edges.
**Lec file**
# Lecture 4.4 - Depth First Search (DFS)_.pdf (PDF file)
![Alt text](<./Lecture 4.4 - Depth First Search (DFS)_.pdf>){ type=application/pdf style="min-height:100vh;width:100%" }