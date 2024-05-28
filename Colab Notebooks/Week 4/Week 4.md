```python
class Queue:
    def __init__(self):
        self.queue = []

    def addq(self, v):
        self.queue.append(v)

    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v

    def isempty(self):
        return self.queue == []

    def __str__(self):
        return str(self.queue)
```


```python
q = Queue()

for i in range(3):
    q.addq(i)
    print(q)
print(q.isempty())

for j in range(3):
    print(q.delq(), q)
print(q.isempty())
```

    [0]
    [0, 1]
    [0, 1, 2]
    False
    0 [1, 2]
    1 [2]
    2 []
    True


### Adjacency matrix example


```python
edges = [
    (0, 1),
    (0, 4),
    (1, 2),
    (2, 0),
    (3, 4),
    (3, 6),
    (4, 0),
    (4, 3),
    # edges = [(0,1),(1,2),(2,0),
    #         (3,4),(3,6),(4,3),
    (4, 7),
    (5, 3),
    (5, 7),
    (6, 5),
    (7, 4),
    (7, 8),
    #        (8,9),(9,8)]
    (8, 5),
    (8, 9),
    (9, 8),
]
uedges = edges + [(j, i) for (i, j) in edges]
```


```python
size = 8
import numpy as np

A = np.zeros(shape=(size, size))
for i, j in edges:
    A[i, j] = 1
print(A)
```

    [[0. 0. 1. 1. 1. 0. 0. 0.]
     [0. 0. 1. 0. 0. 0. 0. 1.]
     [0. 0. 0. 0. 0. 1. 0. 0.]
     [0. 0. 0. 0. 0. 1. 0. 1.]
     [0. 0. 0. 0. 0. 0. 0. 1.]
     [0. 0. 0. 0. 0. 0. 1. 0.]
     [0. 0. 0. 0. 0. 0. 0. 1.]
     [0. 0. 0. 0. 0. 0. 0. 0.]]



```python
def neighbours(AMat, i):
    nbrs = []
    (rows, cols) = AMat.shape
    for j in range(cols):
        if AMat[i, j] == 1:
            nbrs.append(j)
    return nbrs
```


```python
neighbours(A, 7)
```




    [4, 5, 8]



### Adjacency list example


```python
size = 8
AL = {}
for i in range(size):
    AL[i] = []
for i, j in edges:
    AL[i].append(j)
print(AL)
```

    {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}


### BFS


```python
def BFS(AMat, v):
    (rows, cols) = AMat.shape
    visited = {}
    for i in range(rows):
        visited[i] = False
    q = Queue()

    visited[v] = True
    q.addq(v)

    while not q.isempty():
        j = q.delq()
        for k in neighbours(AMat, j):
            if not visited[k]:
                visited[k] = True
                q.addq(k)

    return visited
```


```python
BFS(A, 0), A
```




    ({0: True,
      1: True,
      2: True,
      3: True,
      4: True,
      5: True,
      6: True,
      7: True,
      8: True,
      9: True},
     array([[0., 1., 0., 0., 1., 0., 0., 0., 0., 0.],
            [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 1., 0., 1., 0., 0., 0.],
            [1., 0., 0., 1., 0., 0., 0., 1., 0., 0.],
            [0., 0., 0., 1., 0., 0., 0., 1., 0., 0.],
            [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
            [0., 0., 0., 0., 1., 0., 0., 0., 1., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
            [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.]]))




```python
def BFSList(AList, v):
    visited = {}
    for i in AList.keys():
        visited[i] = False
    q = Queue()

    visited[v] = True
    q.addq(v)

    while not q.isempty():
        j = q.delq()
        for k in AList[j]:
            if not visited[k]:
                visited[k] = True
                q.addq(k)

    return visited
```


```python
BFSList(AL, 0)
```




    {0: True,
     1: True,
     2: True,
     3: True,
     4: True,
     5: True,
     6: True,
     7: True,
     8: True,
     9: True}




```python
def BFSListPath(AList, v):
    (visited, parent) = ({}, {})
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    q = Queue()

    visited[v] = True
    q.addq(v)

    while not q.isempty():
        j = q.delq()
        for k in AList[j]:
            if not visited[k]:
                visited[k] = True
                parent[k] = j
                q.addq(k)

    return (visited, parent)
```


```python
BFSListPath(AL, 0), AL
```




    (({0: True,
       1: True,
       2: True,
       3: True,
       4: True,
       5: True,
       6: True,
       7: True,
       8: True,
       9: True},
      {0: -1, 1: 0, 2: 1, 3: 4, 4: 0, 5: 6, 6: 3, 7: 4, 8: 7, 9: 8}),
     {0: [1, 4],
      1: [2],
      2: [0],
      3: [4, 6],
      4: [0, 3, 7],
      5: [3, 7],
      6: [5],
      7: [4, 8],
      8: [9],
      9: [8]})




```python
def BFSListPathLevel(AList, v):
    (level, parent) = ({}, {})
    for i in AList.keys():
        level[i] = -1
        parent[i] = -1
    q = Queue()

    level[v] = 0
    q.addq(v)

    while not q.isempty():
        j = q.delq()
        for k in AList[j]:
            if level[k] == -1:
                level[k] = level[j] + 1
                parent[k] = j
                q.addq(k)

    return (level, parent)
```


```python
BFSListPathLevel(AL, 0)
```




    ({0: 0, 1: 1, 2: 2, 3: 2, 4: 1, 5: 4, 6: 3, 7: 2, 8: 3, 9: 4},
     {0: -1, 1: 0, 2: 1, 3: 4, 4: 0, 5: 6, 6: 3, 7: 4, 8: 7, 9: 8})



### DFS


```python
def DFSInit(AMat):
    # Initialization
    (rows, cols) = AMat.shape
    (visited, parent) = ({}, {})
    for i in range(rows):
        visited[i] = False
        parent[i] = -1
    return (visited, parent)


def DFS(AMat, visited, parent, v):
    visited[v] = True

    for k in neighbours(AMat, v):
        if not visited[k]:
            parent[k] = v
            (visited, parent) = DFS(AMat, visited, parent, k)

    return (visited, parent)
```


```python
(v, p) = DFSInit(A)
DFS(A, v, p, 3)
```




    ({0: True,
      1: True,
      2: True,
      3: True,
      4: True,
      5: True,
      6: True,
      7: True,
      8: True,
      9: True},
     {0: 4, 1: 0, 2: 1, 3: -1, 4: 3, 5: 6, 6: 3, 7: 4, 8: 7, 9: 8})




```python
def DFSInitList(AList):
    # Initialization
    (visited, parent) = ({}, {})
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    return (visited, parent)


def DFSList(AList, visited, parent, v):
    visited[v] = True

    for k in AList[v]:
        if not visited[k]:
            parent[k] = v
            (visited, parent) = DFSList(AList, visited, parent, k)

    return (visited, parent)
```


```python
(v, p) = DFSInitList(AL)
DFSList(AL, v, p, 3)
```




    ({0: True,
      1: True,
      2: True,
      3: True,
      4: True,
      5: True,
      6: True,
      7: True,
      8: True,
      9: True},
     {0: 4, 1: 0, 2: 1, 3: -1, 4: 3, 5: 6, 6: 3, 7: 4, 8: 7, 9: 8})




```python
(visited, parent) = ({}, {})


def DFSInitGlobal(AMat):
    # Initialization
    (rows, cols) = AMat.shape
    for i in range(rows):
        visited[i] = False
        parent[i] = -1
    return


def DFSGlobal(AMat, v):
    visited[v] = True

    for k in neighbours(AMat, v):
        if not visited[k]:
            parent[k] = v
            DFSGlobal(AMat, k)

    return
```


```python
DFSInitGlobal(A)
DFSGlobal(A, 3)
(visited, parent)
```




    ({3: True,
      0: True,
      1: True,
      2: True,
      4: True,
      5: True,
      6: True,
      7: True,
      8: True,
      9: True},
     {0: 4, 1: 0, 2: 1, 3: -1, 4: 3, 5: 6, 6: 3, 7: 4, 8: 7, 9: 8})




```python
(visited, parent) = ({}, {})


def DFSInitListGlobal(AList):
    # Initialization
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    return


def DFSListGlobal(AList, v):
    visited[v] = True

    for k in AList[v]:
        if not visited[k]:
            parent[k] = v
            DFSListGlobal(AList, k)

    return
```


```python
DFSInitListGlobal(AL)
DFSListGlobal(AL, 3)
(visited, parent)
```




    ({0: True,
      1: True,
      2: True,
      3: True,
      4: True,
      5: True,
      6: True,
      7: True,
      8: True,
      9: True},
     {0: 4, 1: 0, 2: 1, 3: -1, 4: 3, 5: 6, 6: 3, 7: 4, 8: 7, 9: 8})




```python
def Components(AList):
    component = {}
    for i in AList.keys():
        component[i] = -1

    (compid, seen) = (0, 0)

    while seen < max(AList.keys()):
        startv = min([i for i in AList.keys() if component[i] == -1])
        visited = BFSList(AList, startv)
        for i in visited.keys():
            if visited[i]:
                seen = seen + 1
                component[i] = compid
        compid = compid + 1

    return component
```


```python
Components(AL)
```




    {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}




```python
(visited, pre, post) = ({}, {}, {})


def DFSInitPrePost(AList):
    # Initialization
    for i in AList.keys():
        visited[i] = False
        (pre[i], post[i]) = (-1, -1)
    return


def DFSListPrePost(AList, v, count):
    visited[v] = True
    pre[v] = count
    count = count + 1

    for k in AList[v]:
        if not visited[k]:
            count = DFSListPrePost(AList, k, count)
    post[v] = count
    count = count + 1

    return count
```


```python
DFSInitPrePost(AL)
DFSListPrePost(AL, 0, 0)
AL, (visited, pre, post)
```




    ({0: [1, 4],
      1: [0],
      2: [],
      3: [],
      4: [0, 8, 9],
      5: [],
      6: [],
      7: [],
      8: [4, 9],
      9: [8, 4]},
     ({0: True,
       1: True,
       2: False,
       3: False,
       4: True,
       5: False,
       6: False,
       7: False,
       8: True,
       9: True},
      {0: 0, 1: 1, 2: -1, 3: -1, 4: 3, 5: -1, 6: -1, 7: -1, 8: 4, 9: 5},
      {0: 9, 1: 2, 2: -1, 3: -1, 4: 8, 5: -1, 6: -1, 7: -1, 8: 7, 9: 6}))




```python
edges = [(0, 1), (1, 0), (0, 4), (4, 0), (4, 8), (8, 4), (8, 9), (9, 8), (4, 9), (9, 4)]
```


```python
def toposort(AMat):
    (rows, cols) = AMat.shape
    indegree = {}
    toposortlist = []

    for c in range(cols):
        indegree[c] = 0
        for r in range(rows):
            if AMat[r, c] == 1:
                indegree[c] = indegree[c] + 1

    for i in range(rows):
        j = min([k for k in range(cols) if indegree[k] == 0])
        toposortlist.append(j)
        indegree[j] = indegree[j] - 1
        for k in range(cols):
            if AMat[j, k] == 1:
                indegree[k] = indegree[k] - 1

    return toposortlist
```


```python
def toposortlist(AList):
    (indegree, toposortlist) = ({}, [])
    zerodegreeq = Queue()

    for u in AList.keys():
        indegree[u] = 0

    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v] + 1

    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.addq(u)

    while not zerodegreeq.isempty():
        j = zerodegreeq.delq()
        toposortlist.append(j)
        indegree[j] = indegree[j] - 1
        for k in AList[j]:
            indegree[k] = indegree[k] - 1
            if indegree[k] == 0:
                zerodegreeq.addq(k)

    return toposortlist
```


```python
edges = [
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 2),
    (1, 7),
    (2, 5),
    (3, 5),
    (3, 7),
    (4, 7),
    (5, 6),
    (6, 7),
]
```


```python
toposort(A)
```




    [0, 1, 2, 3, 4, 5, 6, 7]




```python
toposortlist(AL)
```




    [0, 1, 3, 4, 2, 5, 6, 7]




```python
def longestpathlist(AList):
    (indegree, lpath) = ({}, {})
    zerodegreeq = Queue()

    for u in AList.keys():
        (indegree[u], lpath[u]) = (0, 0)

    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v] + 1

    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.addq(u)

    while not zerodegreeq.isempty():
        j = zerodegreeq.delq()
        indegree[j] = indegree[j] - 1
        for k in AList[j]:
            indegree[k] = indegree[k] - 1
            lpath[k] = max(lpath[k], lpath[j] + 1)
            if indegree[k] == 0:
                zerodegreeq.addq(k)

    return lpath
```


```python
longestpathlist(AL)
```




    {0: 0, 1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 3, 7: 4}


