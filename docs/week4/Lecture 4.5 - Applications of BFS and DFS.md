# Lecture 4.5 - Applications of BFS and DFS.pdf (PDF file)
**Summary**
BFS and DFS are graph traversal algorithms that provide insights into a graph's structure and connectivity. Here's a summary of their applications: 

1. Connectivity: 
 - BFS can identify connected components in an undirected graph, which are maximal sets of vertices that can reach each other. 
 - DFS numbering can help determine if a directed graph is strongly connected, meaning there is a path between every pair of vertices in both directions. 

2. Cycles: 
 - Non-tree edges in a BFS or DFS tree indicate the presence of cycles in a graph. In a directed graph, only back edges (edges from a vertex to an ancestor in the DFS tree) create cycles. 

3. Strongly Connected Components (SCCs): 
 - DFS numbering can be used to decompose directed graphs into SCCs, where each component consists of vertices that are strongly connected to each other. 

4. Acyclic Graphs: 
 - Directed acyclic graphs (DAGs) have no cycles and are useful for representing dependencies. 
 - Topological sorting, which finds a valid order for completing tasks with dependencies, can be performed using DFS on DAGs. 

5. Other Features: 
 - DFS can also identify articulation points (vertices whose removal would disconnect the graph) and bridges (edges whose removal would disconnect the graph). 

6. Course Scheduling: 
 - Given a set of courses with prerequisites, DFS can be used to find a valid sequence for completing the courses without violating any prerequisites.
**Lec file**
# Lecture 4.5 - Applications of BFS and DFS.pdf (PDF file)
![Alt text](<./Lecture 4.5 - Applications of BFS and DFS.pdf>){ type=application/pdf style="min-height:100vh;width:100%" }