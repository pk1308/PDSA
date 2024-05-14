# Lecture 4.2 - Representing Graphs_.pdf (PDF file)
**Summary**
**Graph Representation**

* Graphs represent relationships between objects (vertices) and connections between them (edges).
* The adjacency matrix method represents graphs using a table where each row and column corresponds to a vertex.
* The adjacency list method stores vertices in a list, with each vertex having a list of its edges to other vertices.

**Representing Graphs for Computing**

* Adjacency lists are more space-efficient than adjacency matrices.
* Adjacency lists are more efficient for determining whether one vertex is a neighbor of another.
* Adjacency matrices are more efficient for identifying all the neighbors of a vertex.

**Checking Reachability**

* To check if one vertex is reachable from another, we can:
    * Mark the target vertex as reachable.
    * Mark all neighbors of reachable vertices as reachable.
    * Repeat until the target vertex is marked or the entire graph has been explored.

**Breadth-First Search vs. Depth-First Search**

* Breadth-first search explores all vertices at a given depth before moving on to the next depth.
* Depth-first search explores a single path as far as possible before backtracking and trying another path.
**Lec file**
# Lecture 4.2 - Representing Graphs_.pdf (PDF file)
![Alt text](<./Lecture 4.2 - Representing Graphs_.pdf>){ type=application/pdf style="min-height:100vh;width:100%" }