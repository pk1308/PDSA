# Lecture 4.4 - Depth First Search (DFS)_.pdf (PDF file)
**Summary**
## Depth First Search (DFS)

DFS is a systematic strategy to explore a graph. It starts from a vertex, visits an unexplored neighbor, suspends the exploration of the current vertex, and explores the neighbor instead. It continues until it reaches a vertex with no unexplored neighbors. DFS then backtracks to the nearest suspended vertex that still has an unexplored neighbor.

### Key Concepts

* **Stack:** DFS uses a stack to store suspended vertices. The most recently suspended vertex is checked first.
* **Visited:** A boolean array to mark visited vertices.
* **Parent:** An array that stores the parent of each vertex.

### Implementation

DFS can be implemented using recursion or iteration.

**Recursive Implementation:**

```python
def DFS(AMat, visited, parent, v):
  visited[v] = True
  for k in neighbors(AMat, v):
    if not visited[k]:
      parent[k] = v
      DFS(AMat, visited, parent, k)
```

**Iterative Implementation:**

```python
def DFS(AMat, visited, parent, v):
  stack = [v]
  while stack:
    v = stack.pop()
    if not visited[v]:
      visited[v] = True
      for k in neighbors(AMat, v):
        if not visited[k]:
          parent[k] = v
          stack.append(k)
```

### Complexity

The complexity of DFS is:

* O(n²) using an adjacency matrix.
* O(m + n) using an adjacency list.

### Applications

DFS is used in:

* Finding connected components in a graph.
* Finding cycles in a graph.
* Topological sorting.
* Finding the minimum spanning tree of a graph.
* Solving mazes.
* Detecting deadlocks in multithreaded programs.

### Advantages

* DFS is easy to implement.
* DFS can explore graphs with cycles.
* DFS can find the shortest path between two vertices.

### Disadvantages

* DFS can produce non-optimal solutions.
* DFS can require more memory than BFS.
* DFS can get stuck in deep paths.
