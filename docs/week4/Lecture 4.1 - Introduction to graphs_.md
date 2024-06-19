# Lecture 4.1 - Introduction to graphs_.pdf (PDF file)
**Summary**
## Introduction to Graphs

**Definition:** A graph is a data structure that represents a set of objects (called vertices or nodes) and a set of relationships (called edges) between those objects.

**Components:**
* **Vertices:** Entities or objects of interest.
* **Edges:** Connections or relationships between vertices.

**Types of Graphs:**

* **Directed graphs:** Edges have a direction, indicating a one-way relationship between vertices.
* **Undirected graphs:** Edges do not have a direction, indicating a bidirectional relationship between vertices.

## Paths and Reachability

**Path:** A sequence of vertices connected by edges.

**Reachability:** Determining whether there exists a path from one vertex to another in a directed graph.

## Graph Applications

Graphs are widely used in various applications, including:

* **Map coloring:** Determining the minimum number of colors needed to color a map without adjacent regions having the same color.
* **Vertex cover:** Finding the minimum number of vertices that cover all edges in a graph.
* **Independent set:** Identifying a subset of vertices that are not connected by any edges.
* **Matching:** Assigning pairs of vertices (e.g., people, projects) based on compatibility or availability.

## Graph Representation in Python

In Python, graphs can be represented using various data structures, including:

* **Adjacency list:** A dictionary where each key represents a vertex and the corresponding value is a list of adjacent vertices.
* **Adjacency matrix:** A 2D array where the rows and columns represent vertices, and a non-zero value indicates an edge between the corresponding vertices.
* **NetworkX library:** A dedicated library for graph manipulation and analysis.

## Graph Traversal and Search

**Depth-first search (DFS):** Traverses a graph by following edges until a dead end is reached, then backtracking to explore other paths.

**Breadth-first search (BFS):** Traverses a graph by visiting all vertices at the same level before moving to the next level.

## Minimum Spanning Tree

A minimum spanning tree is a subgraph of a connected graph that includes all vertices but has the minimum possible total edge weight.

## Shortest Path

Finding the shortest path between two vertices in a graph is a fundamental graph problem with numerous applications, such as route planning and network optimization.

## Graph Optimization Problems

Graphs can also be used to solve optimization problems, such as:

* **Maximum flow:** Determining the maximum amount of flow that can pass through a network.
* **Minimum cut:** Partitioning a graph into two disjoint sets while minimizing the number of edges between them.
* **Traveling salesman problem:** Finding the shortest possible path that visits a set of cities and returns to the starting city.
**Lec file**
# Lecture 4.1 - Introduction to graphs_.pdf (PDF file)
![Alt text](<./Lecture 4.1 - Introduction to graphs_.pdf>){ type=application/pdf style="min-height:100vh;width:100%" }