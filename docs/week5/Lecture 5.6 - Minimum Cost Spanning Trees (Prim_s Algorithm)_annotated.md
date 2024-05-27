# Lecture 5.6 - Minimum Cost Spanning Trees (Prim_s Algorithm)_annotated.pdf (PDF file)
**Summary**
Prim's algorithm is a technique used to generate a minimum cost spanning tree (MCST) from a given weighted undirected graph. An MCST is a tree that spans all vertices in the graph, and has the minimum total edge weight among all such trees. 

The algorithm incrementally grows the MCST by adding the smallest weight edge from the tree to a vertex not yet in the tree. It begins with a single vertex and expands until it includes all vertices while adhering to the MCST principles. 

The correctness of Prim's algorithm is based on the Minimum Separator Lemma, which states that every MCST must include the minimum cost edge separating two non-empty subsets of vertices. This allows the algorithm to efficiently construct the MCST by selecting the smallest weight edge at each step. 

The implementation involves tracking visited vertices, distances to the tree, and the nearest neighbor in the tree for each vertex. By continuously updating this information, the algorithm identifies the next vertex to add to the tree based on the minimum distance criterion. 

Despite its simplicity, Prim's algorithm has a complexity of O(n2), where n is the number of vertices, even with adjacency lists. This is due to the need to repeatedly scan through the unvisited vertices to find the minimum distance. More efficient algorithms exist, such as Kruskal's algorithm, which has a complexity of O(E log E), but Prim's algorithm remains a fundamental and widely used approach for constructing MCSTs.
**Lec file**
# Lecture 5.6 - Minimum Cost Spanning Trees (Prim_s Algorithm)_annotated.pdf (PDF file)
![Alt text](<./Lecture 5.6 - Minimum Cost Spanning Trees (Prim_s Algorithm)_annotated.pdf>){ type=application/pdf style="min-height:100vh;width:100%" }