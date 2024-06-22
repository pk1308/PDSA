```python
import os 
import numpy as np 

```

# first approach 


```python
    
    
# Define the neighbours function
def neighbours(AMat, to_explore):
    """
    Finds the neighbors of a given vertex in a graph represented by an adjacency matrix.

    Parameters:
    AMat: 2D numpy array
        The adjacency matrix representing the graph.
    j: int
        The vertex for which to find the neighbors.

    Returns:
    list:
        A list of neighbors of vertex j.
    """
    neighbors = []
    for i in range(AMat.shape[1]):
        if AMat[to_explore, i] == 1:  # Assuming 1 indicates an edge/connection
            neighbors.append(i)
    return neighbors
    
```


```python
def DFSinit(AMat):
    """
    Initializes the visited and parent dictionaries for Depth-First Search (DFS).

    Parameters:
    AMat : numpy.ndarray
        The adjacency matrix representing the graph.

    Returns:
    visited : dict
        A dictionary where keys are the vertices and values are booleans indicating
        whether the vertex has been visited (True) or not (False).
    parent : dict
        A dictionary where keys are the vertices and values are integers representing
        the parent vertex in the DFS tree, or -1 if no parent (for the starting vertex).
    """
    rows = AMat.shape[0]
    visited = {}
    parent = {}
    
    for i in range(rows):
        visited[i] = False
        parent[i] = -1
        
    return visited, parent



def DFSAmat(Amat , visited  , parent , source_vertex):
    """
    Performs Depth-First Search (BFS) on a graph represented by an adjacency matrix.

    Parameters:
    AMat : list of list
        The adjacency matrix representing the graph.
    visited : dict
        A dictionary where keys are the vertices and values are booleans indicating
        whether the vertex has been visited (True) or not (False).
    parent : dict
        A dictionary where keys are the vertices and values are integers representing
        the parent vertex in the BFS tree, or -1 if no parent (for the source vertex).
    source_vertex : int
        The starting vertex for the BFS.

    Returns:
    visited : dict
        Updated dictionary indicating which vertices have been visited after BFS.
    parent : dict
        Updated dictionary representing the parent vertices after BFS.
    """
    visited[source_vertex] = True 
    
    for neighbour in neighbours(AMat=Amat, to_explore=source_vertex):
        if not visited[neighbour]: 
            parent[neighbour] = source_vertex
            visited , parent = DFSAmat(Amat=Amat, visited=visited,parent=parent, source_vertex=neighbour )
    return visited , parent
        
```


```python
adj_matrix =np.array( [
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0]
])

```


```python
visited , parent = DFSinit(AMat=adj_matrix) 
DFSAmat(adj_matrix, visited , parent , 0 )
```


```python
visited , parent
```




    ({0: False,
      1: False,
      2: False,
      3: False,
      4: False,
      5: False,
      6: False,
      7: False,
      8: False},
     {0: -1, 1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1})




```python
DFSAmat(adj_matrix, visited , parent , 0 )
```




    ({0: True,
      1: True,
      2: True,
      3: True,
      4: True,
      5: True,
      6: True,
      7: True,
      8: True},
     {0: -1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 2, 7: 3, 8: 3})




```python
del visited
del parent
```


```python
visited = {}
parent = {}
def DFSinit(AMat):
    """
    Initializes the visited and parent dictionaries for Depth-First Search (DFS).

    Parameters:
    AMat : numpy.ndarray
        The adjacency matrix representing the graph.

    Returns:
    visited : dict
        A dictionary where keys are the vertices and values are booleans indicating
        whether the vertex has been visited (True) or not (False).
    parent : dict
        A dictionary where keys are the vertices and values are integers representing
        the parent vertex in the DFS tree, or -1 if no parent (for the starting vertex).
    """
    rows = AMat.shape[0]
    global visited
    global parent 
    
    for i in range(rows):
        visited[i] = False
        parent[i] = -1
        
    return visited, parent



def DFSAmat(Amat ,source_vertex):
    """
    Performs Depth-First Search (BFS) on a graph represented by an adjacency matrix.

    Parameters:
    AMat : list of list
        The adjacency matrix representing the graph.
    visited : dict
        A dictionary where keys are the vertices and values are booleans indicating
        whether the vertex has been visited (True) or not (False).
    parent : dict
        A dictionary where keys are the vertices and values are integers representing
        the parent vertex in the BFS tree, or -1 if no parent (for the source vertex).
    source_vertex : int
        The starting vertex for the BFS.

    Returns:
    visited : dict
        Updated dictionary indicating which vertices have been visited after BFS.
    parent : dict
        Updated dictionary representing the parent vertices after BFS.
    """
    global visited
    global parent 
    visited[source_vertex] = True 
    
    for neighbour in neighbours(AMat=Amat, to_explore=source_vertex):
        if not visited[neighbour]: 
            parent[neighbour] = source_vertex
            visited , parent = DFSAmat(Amat=Amat, source_vertex=neighbour )
    return visited , parent
        
```


```python
visited , parent = DFSinit(AMat=adj_matrix) 
DFSAmat(adj_matrix, 0 )
```




    ({0: True,
      1: True,
      2: True,
      3: True,
      4: True,
      5: True,
      6: True,
      7: True,
      8: True},
     {0: -1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 2, 7: 3, 8: 3})




```python
del visited
del parent
```


```python
def create_Alist(AMat):
    AList = {}
    for  parent in range(AMat.shape[0]):
        neighbours = []
        for neighbour in range(AMat.shape[1]):
            if AMat[parent, neighbour] ==1 :
                neighbours.append(neighbour)
        AList[parent] = neighbours
    return AList
```


```python
Alist = create_Alist(adj_matrix)
```


```python
visited = {}
parent = {}
def DFSinit(AList):
    """
    Initializes the visited and parent dictionaries for Depth-First Search (DFS).

    Parameters:
    AMat : numpy.ndarray
        The adjacency matrix representing the graph.

    Returns:
    visited : dict
        A dictionary where keys are the vertices and values are booleans indicating
        whether the vertex has been visited (True) or not (False).
    parent : dict
        A dictionary where keys are the vertices and values are integers representing
        the parent vertex in the DFS tree, or -1 if no parent (for the starting vertex).
    """
    global visited
    global parent 
    
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
        
    return visited, parent



def DFSList(AList ,source_vertex):
    """
    Performs Depth-First Search (BFS) on a graph represented by an adjacency matrix.

    Parameters:
    AMat : list of list
        The adjacency matrix representing the graph.
    visited : dict
        A dictionary where keys are the vertices and values are booleans indicating
        whether the vertex has been visited (True) or not (False).
    parent : dict
        A dictionary where keys are the vertices and values are integers representing
        the parent vertex in the BFS tree, or -1 if no parent (for the source vertex).
    source_vertex : int
        The starting vertex for the BFS.

    Returns:
    visited : dict
        Updated dictionary indicating which vertices have been visited after BFS.
    parent : dict
        Updated dictionary representing the parent vertices after BFS.
    """
    global visited
    global parent 
    visited[source_vertex] = True 
    
    for neighbour in  AList[source_vertex]:
        if not visited[neighbour]: 
            parent[neighbour] = source_vertex
            visited , parent = DFSAmat(AList=AList, source_vertex=neighbour )
    return visited , parent
        
```


```python
visited , parent = DFSinit(AList=Alist)

DFSList(AList=Alist , source_vertex=0 )
```




    ({0: True,
      1: True,
      2: True,
      3: True,
      4: True,
      5: True,
      6: True,
      7: True,
      8: True},
     {0: -1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 2, 7: 3, 8: 3})




```python

```
