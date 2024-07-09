# Lecture 5.5 - Minimum Cost Spanning Trees_annotated.pdf (PDF file)
**Summary**
## Minimum Cost Spanning Trees (MCSTs)

### Overview

In a network, a spanning tree is a subset of the edges that connects all the vertices without creating any cycles. When each edge has an associated cost, the goal of finding a minimum cost spanning tree (MCST) is to select the spanning tree with the lowest total cost.

### Applications

MCSTs have numerous applications in real-world scenarios:

- **Infrastructure planning:** Designing road networks, power grids, or communication systems by minimizing the total cost of connecting all locations.
- **Cable redundancy:** Ensuring that there are redundant network connections by adding a minimum number of backup cables to an existing fiber optic network.

### Spanning Trees

A spanning tree is a tree that connects all the vertices in a graph. Key facts about trees include:

- A tree with n vertices has exactly n-1 edges.
- Adding an edge to a tree creates a cycle.
- Every pair of vertices in a tree is connected by a unique path.

### Building Minimum Cost Spanning Trees

Two primary algorithms for finding MCSTs are:

1. **Prim's algorithm:** Starts with the smallest edge and gradually adds edges that connect components without creating cycles.
2. **Kruskal's algorithm:** Sorts edges in ascending order of weight and then connects components in that order, avoiding cycles.

### Prim's Algorithm

**Steps:**

1. Initialize a set S to contain a single vertex.
2. While S does not contain all vertices:
    - Find the lowest-cost edge (u, v) that connects a vertex in S to a vertex not in S.
    - Add (u, v) to S.

### Kruskal's Algorithm

**Steps:**

1. Sort the edges in ascending order of weight.
2. Create a set of disjoint sets, each containing a single vertex.
3. For each edge (u, v) in order:
    - If u and v are in different sets:
        - Add (u, v) to the MCST.
        - Merge the sets containing u and v.
