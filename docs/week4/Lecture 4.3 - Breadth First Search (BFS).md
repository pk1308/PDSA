# Lecture 4.3 - Breadth First Search (BFS).pdf (PDF file)
**Summary**
Breadth First Search (BFS) is an algorithm used to traverse and search a graph or tree data structure. It starts at a specified starting node and explores all reachable nodes, level by level, before moving on.

Here's a summary of the BFS algorithm:

1. **Initialization:**
    - Mark the starting node as visited.
    - Create a queue and add the starting node to it.

2. **Exploration:**
    - While the queue is not empty:
        - Remove the first node from the queue.
        - Visit the node and perform any necessary operations.
        - Add all unvisited neighbors of the node to the queue.

3. **Termination:**
    - The algorithm continues until the queue is empty, indicating that all reachable nodes have been visited.

BFS has several key characteristics:

- **Level-by-level exploration:** BFS explores nodes level by level, starting with the starting node and moving outward.
- **Queue-based:** It uses a queue to keep track of nodes that have been visited but not yet explored.
- **Complexity:** The time complexity of BFS is typically O(n+m), where n is the number of nodes and m is the number of edges in the graph.

BFS can be used to solve a variety of graph-related problems, including finding the shortest path between two nodes, detecting cycles, and checking for connectivity.
**Lec file**
# Lecture 4.3 - Breadth First Search (BFS).pdf (PDF file)
![Alt text](<./Lecture 4.3 - Breadth First Search (BFS).pdf>){ type=application/pdf style="min-height:100vh;width:100%" }