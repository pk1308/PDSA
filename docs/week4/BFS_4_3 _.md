```python
import os
import numpy as np

```

# Queue 


```python

class Queue:
    def __init__(self):
        """
        Initializes an empty queue.
        The queue is represented as a list.
        """
        self.queue = []

    def Equeue(self, v):
        """
        Adds an element 'v' to the end of the queue.

        Parameters:
        v: The element to be added to the queue.
        """
        self.queue.append(v)

    def Dqueue(self):
        """
        Removes and returns the element at the front of the queue.

        Returns:
        The element at the front of the queue if the queue is not empty,
        otherwise None.
        """
        v = None
        if not self.isempty():
            v = self.queue[0]  
            self.queue = self.queue[1:]  
        return v

    def isempty(self):
        """
        Checks if the queue is empty.

        Returns:
        True if the queue is empty, otherwise False.
        """
        return self.queue == []

    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
        A string representation of the queue list.
        """
        return str(self.queue)
```


```python
AMat = np.array(
    [
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    ]
)
```


```python
def BFSMat( AMat , source_vertex ):
    
    """
    Performs Breadth-First Search (BFS) on a graph represented by an adjacency matrix.

    Parameters:
    AMat: 2D numpy array
        The adjacency matrix representing the graph.
    Source_vertex : int
        The starting vertex for the BFS.

    Returns:
    visited: dict
        A dictionary where keys are the vertices and values are booleans indicating
        whether the vertex has been visited (True) or not (False).
        """
    rows , cols = AMat.shape
    visited = {i : False for i in range(rows)
               }
    visited[source_vertex] = True 
    
    q = Queue()
    q.Equeue(source_vertex)
    while not q.isempty():
        to_explore = q.Dqueue()
        for neighbour in neighbours(AMat=AMat , to_explore=to_explore):
            if not visited[neighbour]:
                visited[neighbour] = True 
                q.Equeue(neighbour)
    return visited
            
    
    
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
AMat = np.array([[0, 1, 0, 0],
                 [1, 0, 1, 0], 
                 [0, 1, 0, 1], 
                 [0, 0, 1, 0]])

# Starting vertex
v = 0

# Perform BFS
visited = BFSMat(AMat, v)
print(visited)
```

    {0: True, 1: True, 2: True, 3: True}



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
def BFSAlist( AList , source_vertex ):
    
    """
    Performs Breadth-First Search (BFS) on a graph represented by an adjacency matrix.

    Parameters:
    AMat: 2D numpy array
        The adjacency matrix representing the graph.
    Source_vertex : int
        The starting vertex for the BFS.

    Returns:
    visited: dict
        A dictionary where keys are the vertices and values are booleans indicating
        whether the vertex has been visited (True) or not (False).
        """
    visited = {i : False for i in AList.keys() }
    visited[source_vertex] = True 
    
    q = Queue()
    q.Equeue(source_vertex)
    while not q.isempty():
        to_explore = q.Dqueue()
        for neighbour in AList[to_explore]:
            if not visited[neighbour]:
                visited[neighbour] = True 
                q.Equeue(neighbour)
    return visited
```


```python
Alist = create_Alist(AMat)
```


```python
Alist
```




    {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}




```python
BFSAlist(Alist,source_vertex=v)
```




    {0: True, 1: True, 2: True, 3: True}




```python
class Queue:
    def __init__(self):
        """
        Initializes an empty queue.
        The queue is represented as a list.
        """
        self.queue = []

    def Enqueue(self, v):
        """
        Adds an element 'v' to the end of the queue.

        Parameters:
        v: The element to be added to the queue.
        """
        self.queue.append(v)

    def Dequeue(self):
        """
        Removes and returns the element at the front of the queue.

        Returns:
        The element at the front of the queue if the queue is not empty,
        otherwise None.
        """
        v = None
        if not self.isempty():
            v = self.queue[0]  
            self.queue = self.queue[1:]  
        return v

    def isempty(self):
        """
        Checks if the queue is empty.

        Returns:
        True if the queue is empty, otherwise False.
        """
        return self.queue == []

    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
        A string representation of the queue list.
        """
        return str(self.queue)
```


```python
def BFSAlistPath(AList, source_vertex):
    """
    Performs Breadth-First Search (BFS) on a graph represented by an adjacency list.

    Parameters:
    AList : dict
        The adjacency list representing the graph. It's a dictionary where keys are vertices
        and values are lists of adjacent vertices.
    source_vertex : int
        The starting vertex for the BFS.

    Returns:
    visited : dict
        A dictionary where keys are the vertices and values are booleans indicating
        whether the vertex has been visited (True) or not (False).
    parent : dict
        A dictionary where keys are the vertices and values are integers representing
        the parent vertex in the BFS tree, or -1 if no parent (for the source vertex).

    Note:
    This function assumes the existence of a Queue data structure with methods `enqueue`
    (to add an item) and `dequeue` (to remove and return the next item), as used in BFS.
    """
    visited = {}
    parent = {}
    
    # Initialize visited and parent dictionaries
    for vertex in AList.keys():
        visited[vertex] = False
        parent[vertex] = -1
        
    # Mark the source vertex as visited
    visited[source_vertex] = True
    
    # Initialize a queue for BFS
    q = Queue()
    q.Enqueue(source_vertex)
    
    # Perform BFS
    while not q.isempty():
        current_vertex = q.Dequeue()
        for neighbour in AList[current_vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                parent[neighbour] = current_vertex
                q.Enqueue(neighbour)
    
    return visited, parent

```


```python
BFSAlistPath(AList=Alist , source_vertex=v)
```




    ({0: True, 1: True, 2: True, 3: True}, {0: -1, 1: 0, 2: 1, 3: 2})




```python
def BFSAlistPathLevel(AList, source_vertex):
    """
    Performs Breadth-First Search (BFS) on a graph represented by an adjacency list,
    and computes the level (distance from the source vertex) for each vertex.

    Parameters:
    AList : dict
        The adjacency list representing the graph. It's a dictionary where keys are vertices
        and values are lists of adjacent vertices.
    source_vertex : int
        The starting vertex for the BFS.

    Returns:
    level : dict
        A dictionary where keys are the vertices and values are integers indicating
        the level (distance from the source vertex) of each vertex.
    parent : dict
        A dictionary where keys are the vertices and values are integers representing
        the parent vertex in the BFS tree, or -1 if no parent (for the source vertex).

    Note:
    This function assumes the existence of a Queue data structure with methods `enqueue`
    (to add an item) and `dequeue` (to remove and return the next item), as used in BFS.
    """
    level = {}
    parent = {}
    
    # Initialize level and parent dictionaries
    for vertex in AList.keys():
        level[vertex] = -1  # -1 indicates vertex has not been visited or reached
        parent[vertex] = -1
        
    # Mark the source vertex with level 0
    level[source_vertex] = 0 
    
    # Initialize a queue for BFS
    q = Queue()
    q.Enqueue(source_vertex)
    
    # Perform BFS
    while not q.isempty():
        current_vertex = q.Dequeue()
        for neighbour in AList[current_vertex]:
            if level[neighbour] == -1:  # Check if neighbour has not been visited
                level[neighbour] = level[current_vertex] + 1
                parent[neighbour] = current_vertex
                q.Enqueue(neighbour)
    print("Level" , level)
    print("parent" , parent)
    return level, parent

```


```python
BFSAlistPathLevel(Alist, v)
```

    Level {0: 0, 1: 1, 2: 2, 3: 3}
    parent {0: -1, 1: 0, 2: 1, 3: 2}





    ({0: 0, 1: 1, 2: 2, 3: 3}, {0: -1, 1: 0, 2: 1, 3: 2})




```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
