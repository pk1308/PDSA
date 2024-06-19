# Lecture 4.3 - Breadth First Search (BFS)_.pdf (PDF file)
**Summary**
**Breadth First Search**

**Reachability in a graph**
- Mark source vertex as reachable
- Systematically mark neighbours of marked
vertices
- Stop when target becomes marked

**Choose an appropriate representation**
- Adjacency matrix
- Adjacency list

**Strategies for systematic exploration**
- Breadth first — propagate marks in
“layers”
- Depth first — explore a path till it dies
out, then backtrack

**Breadth First Search (BFS)**
- Explore the graph level by level
- First visit vertices one step away
- Then two steps away
- . . .
- Each visited vertex has to be explored

**Breadth first search (BFS)**
- Assume V = {0, 1, . . . , n − 1}
-visited : V → {True, False} tells us
whether v ∈ V has been visited
-Initially, visited(v) = False for all v ∈ V
-Maintain a sequence of visited vertices yet
to be explored
-A queue — first in, first out

**Exploring a vertex i**
- For each edge (i, j), if visited(j) is False,
- Set visited(j) to True
- Append j to the queue

**BFS . . .**
-Assume V = {0, 1, . . . , n − 1}
-visited : V → {True, False} tells us
whether v ∈ V has been visited
-Initially, visited(v) = False for all v ∈ V
-Maintain a sequence of visited vertices yet
to be explored
-A queue — first in, first out
-Exploring a vertex i
- For each edge (i, j), if visited(j) is False,
- Set visited(j) to True
- Append j to the queue

**BFS . . .**
- q = Queue()
-for i in range(3):
- q.addq(i)
-print(q)
-print(q.isempty())
-for j in range(3):
- print(q.delq(),q)
-print(q.isempty())

**BFS . . .**
-Initially
-visited(v) = False for all v ∈ V
-Queue of vertices to be explored is empty
-Start BFS from vertex j
-Set visited(j) = True
-Add j to the queue
-Remove and explore vertex i at head of
queue
-For each edge (i, j), if visited(j) is False,
- Set visited(j) to True
- Append j to the queue
-Stop when queue is empty

**BFS from vertex 7**
-Visited
0 False
1 False
2 False
3 False
4 False
5 False
6 False
7 False
8 False
9 False
-To explore queue
-Mark 7 and add to queue

**BFS from vertex 7**
-Visited
0 True
1 False
2 False
3 False
4 False
5 False
6 False
7 True
8 False
9 False
-To explore queue
-7

**BFS from vertex 7**
-Visited
0 True
1 False
2 False
3 False
4 True
5 True
6 False
7 True
8 True
9 False
-To explore queue
-4 5 8

**BFS from vertex 7**
-Visited
0 True
1 False
2 False
3 True
4 True
5 True
6 False
7 True
8 True
9 False
-To explore queue
-5 8 0 3

**BFS from vertex 7**
-Visited
0 True
1 False
2 False
3 True
4 True
5 True
6 True
7 True
8 True
9 False
-To explore queue
-8 0 3 6

**BFS from vertex 7**
-Visited
0 True
1 True
2 True
3 True
4 True
5 True
6 True
7 True
8 True
9 False
-To explore queue
-0 3 6 9

**BFS from vertex 7**
-Visited
0 True
1 True
2 True
3 True
4 True
5 True
6 True
7 True
8 True
9 True
-To explore queue
-3 6 9 1 2

**BFS from vertex 7**
-Visited
0 True
1 True
2 True
3 True
4 True
5 True
6 True
7 True
8 True
9 True
-To explore queue
-6 9 1 2

**BFS from vertex 7**
-Visited
0 True
1 True
2 True
3 True
4 True
5 True
6 True
7 True
8 True
9 True
-To explore queue
-9 1 2

**BFS from vertex 7**
-Visited
0 True
1 True
2 True
3 True
4 True
5 True
6 True
7 True
8 True
9 True
-To explore queue
-1 2

**BFS from vertex 7**
-Visited
0 True
1 True
2 True
3 True
4 True
5 True
6 True
7 True
8 True
9 True
-To explore queue
-2

**BFS from vertex 7**
-Visited
0 True
1 True
2 True
3 True
4 True
5 True
6 True
7 True
8 True
9 True
-To explore queue

**Complexity of BFS**
-G = (V, E)
-|V| = n
-|E| = m
-If G is connected, m can vary from
n − 1 to n(n − 1)/2
-In BFS, each reachable vertex is
processed exactly once
-Visit the vertex: add to queue
-Explore the vertex: remove from queue
-Visit and explore at most n vertices
-Exploring a vertex
-Check all outgoing edges
-How long does this take?

**Complexity of BFS**
-G = (V, E)
-|V| = n
-|E| = m
-If G is connected, m can vary from
n − 1 to n(n − 1)/2
-In BFS, each reachable vertex is
processed exactly once
-Visit the vertex: add to queue
-Explore the vertex: remove from queue
-Visit and explore at most n vertices
-Exploring a vertex
-Check all outgoing edges
-How long does this take?

**Complexity of BFS**
-G = (V, E)
-|V| = n
-|E| = m
-If G is connected, m can vary from
n − 1 to n(n − 1)/2
-In BFS, each reachable vertex is
processed exactly once
-Visit the vertex: add to queue
-Explore the vertex: remove from queue
-Visit and explore at most n vertices
-Exploring a vertex
-Check all outgoing edges
-How long does this take?

**Complexity of BFS**
-Adjacency matrix
-To explore i, scan neighbours(i)
-Look up n entries in row i, regardless of
degree(i)

**Complexity of BFS**
-Adjacency matrix
-To explore i, scan neighbours(i)
-Look up n entries in row i, regardless of
degree(i)
-Adjacency list
-List neighbours(i) is directly available
-Time to explore i is degree(i)
-Degree varies across vertices

**Complexity of BFS**
-BFS with adjacency matrix
-n steps to initialize each vertex
-n steps to explore each vertex
-Overall time is O(n\r\n2\r\n)

**Complexity of BFS**
-BFS with adjacency matrix
-n steps to initialize each vertex
-n steps to explore each vertex
-Overall time is O(n\r\n2\r\n)
-BFS with adjacency list
-n steps to initialize each vertex
-2m steps (sum of degrees) to explore all
vertices
-An example of amortized analysis
-Overall time is O(n + m)

**Complexity of BFS**
-If m \x1c n\r\n2\r\n, working with adjacency lists
is much more efficient
-This is why we treat m and n as
separate parameters
-For graphs, O(m + n) is typically the
best possible complexity
-Need to see each each vertex and edge
at least once
-Linear time

**Enhancing BFS to record paths**
-If BFS from i sets visited(k) = True, we
know that k is reachable from i
-How do we recover a path from i to k?
-visited(k) was set to True when exploring
some vertex j
-Record parent(k) = j
-From k, follow parent links to trace back
a path to i

**Enhancing BFS to record paths**
-If BFS from i sets visited(k) = True, we
know that k is reachable from i
-How do we recover a path from i to k?
-visited(k) was set to True when exploring
some vertex j
-Record parent(k) = j
-From k, follow parent links to trace back
a path to i

**
