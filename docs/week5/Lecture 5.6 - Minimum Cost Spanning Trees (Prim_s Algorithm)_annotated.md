# Lecture 5.6 - Minimum Cost Spanning Trees (Prim_s Algorithm)_annotated.pdf (PDF file)
**Summary**
**Minimum Cost Spanning Trees**

**Definition:**
A Minimum Cost Spanning Tree (MCST) of a weighted, undirected graph is a spanning tree with the minimum possible total edge weight.

**Strategy:**
Prim's algorithm incrementally grows an MCST by adding the smallest edge from the current tree to a vertex not yet in the tree.

**Correctness:**
The Minimum Separator Lemma states that every MCST must include the minimum cost edge between any two non-empty subsets of vertices. Since Prim's algorithm always selects the smallest edge connecting the tree to outside vertices, it guarantees an MCST.

**Implementation:**

* Initialize visited[v] to False and distance[v] to infinity for all vertices.
* Mark a starting vertex as visited and set its distance to 0.
* For each iteration:
    * Find the unvisited vertex with the smallest distance to the tree.
    * Add that vertex to the tree and update the distances of its neighbors to the tree.
* Return the edges in the spanning tree.

**Improved Implementation:**

* Keep track of the nearest neighbor of each vertex in the tree.
* Scan all non-tree vertices to find the next vertex with minimum distance to the tree.
* This optimization reduces the complexity to O(n) per iteration.

**Complexity:**

* The original implementation takes O(n^2) time.
* The improved implementation takes O(n^2) time with an adjacency matrix and O(n log n) time with an adjacency list.

**Summary:**

* Prim's algorithm constructs an MCST incrementally.
* The Minimum Separator Lemma ensures its correctness.
* The improved implementation reduces the complexity to O(n^2) or O(n log n) depending on the data structure used.
* The bottleneck lies in efficiently identifying the vertex with the smallest distance to the tree.
