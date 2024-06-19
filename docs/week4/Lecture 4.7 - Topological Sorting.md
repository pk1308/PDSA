# Lecture 4.7 - Topological Sorting.pdf (PDF file)
**Summary**
**Topological Sorting**

Topological sorting is a technique used to order the vertices of a directed acyclic graph (DAG) in a way that respects the dependencies between the vertices. A DAG is a directed graph with no directed cycles, meaning that there is no path from any vertex back to itself.

**Applications of Topological Sorting**

Topological sorting has many applications in computer science, including:

* Scheduling tasks that have dependencies
* Finding the order of compilation for a set of source files
* Determining the order of execution for a set of instructions in a program
* Resolving conflicts in version control systems

**Algorithm for Topological Sorting**

There are several different algorithms for performing topological sorting. One common algorithm works as follows:

1. Start with an empty list of sorted vertices.
2. Find a vertex with no incoming edges (i.e., a vertex with an indegree of 0).
3. Add the vertex to the sorted list.
4. Delete the vertex and all of its outgoing edges from the graph.
5. Repeat steps 2-4 until all vertices have been added to the sorted list.

**Complexity of Topological Sorting**

The time complexity of topological sorting is O(V + E), where V is the number of vertices in the graph and E is the number of edges.

**Proof of Correctness**

The topological sorting algorithm is correct because it maintains the following invariant:

* The sorted list contains a subset of the vertices in the graph.
* The vertices in the sorted list are ordered in such a way that there are no edges from any vertex in the sorted list to any vertex that is not in the sorted list.

This invariant is established by the following steps in the algorithm:

* When a vertex with no incoming edges is added to the sorted list, it is added to the end of the list. This ensures that there are no edges from any vertex in the sorted list to the newly added vertex.
* When a vertex is deleted from the graph, all of its outgoing edges are also deleted. This ensures that there are no edges from any vertex in the sorted list to any vertex that is not in the sorted list.

**Example**

Consider the following DAG:

```
A -> B
B -> C
C -> D
D -> E
```

The following is a topological sort of this DAG:

```
[A, B, C, D, E]
```

**Additional Notes**

* Topological sorting is not unique. There may be multiple different topological sorts of the same DAG.
* The choice of which vertex to add to the sorted list in step 2 of the algorithm is arbitrary. Any vertex with an indegree of 0 can be added.
* Topological sorting can be used to detect cycles in a directed graph. If the algorithm is unable to find a vertex with an indegree of 0, then the graph contains a cycle.
