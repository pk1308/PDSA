# Lecture 4.2 - Representing Graphs.pdf (PDF file)
**Summary**
**Graph Representation**

Graphs can be represented using two common data structures:

**Adjacency Matrix:**

* A table where each cell (i, j) represents the existence (1) or absence (0) of an edge between vertices i and j.
* Suitable for dense graphs (many edges) as it stores information for all possible pairs of vertices.
* Efficient for checking if two vertices are connected.

**Adjacency List:**

* A dictionary where each key is a vertex, and the associated value is a list of adjacent vertices.
* Suitable for sparse graphs (few edges) as it only stores information for existing edges.
* Efficient for iterating through the neighbors of a vertex.

**Choosing the Right Representation:**

The choice of representation depends on the graph structure and the operations to be performed:

* Adjacency matrix uses more space but is faster for checking connectivity.
* Adjacency list uses less space but requires more computation to check connectivity.

**Reachability Checking:**

* To determine if a vertex (target) is reachable from another vertex (source), systematically mark and propagate the mark to all reachable vertices.
* Depth-first search (DFS) or breadth-first search (BFS) algorithms can be used for this purpose.
* DFS explores paths until they die out and backtracks, while BFS propagates marks in "layers."
**Lec file**
# Lecture 4.2 - Representing Graphs.pdf (PDF file)
![Alt text](<./Lecture 4.2 - Representing Graphs.pdf>){ type=application/pdf style="min-height:100vh;width:100%" }