```python
import os 
import numpy as np 

os.chdir("..")
os.chdir("..")
from driver_folder.time_driver import TimerError 
```


```python
T =TimerError()
T.start()
end_time = T.elapsed()
print(f"time taken:{end_time}")
```

    time taken:2.2519000026477443e-05



```python
import numpy as np

def toposort(AMat):
    """
    Performs a topological sort on a directed acyclic graph (DAG) using an adjacency matrix.
    
    Parameters:
    AMat (np.ndarray): Adjacency matrix representing the graph, where AMat[i][j] == 1 indicates an edge from node i to node j.
    
    Returns:
    list: A list of nodes in topologically sorted order.
    """
    
    # Get the number of rows and columns from the adjacency matrix
    rows, cols = AMat.shape
    
    # Initialize the indegree dictionary and the list to store the topological sort result
    indegree = {}
    toposortlist = []

    # Step 1: Initialize all nodes' indegree to 0
    for c in range(cols):
        indegree[c] = 0
    
    # Step 2: Compute indegree for each node
    for r in range(rows):
        for c in range(cols):
            if AMat[r, c] == 1:
                indegree[c] += 1
    
    # Step 3: Perform the topological sort
    for _ in range(cols):
        # Find a node with zero indegree
        zero_indegree_nodes = [k for k in range(cols) if indegree[k] == 0]
        if not zero_indegree_nodes:
            raise ValueError("Graph has at least one cycle")
        
        # Select the first node with zero indegree
        j = zero_indegree_nodes[0]
        toposortlist.append(j)
        
        # Set the indegree of this node to -1 to mark it as processed
        indegree[j] = -1
        
        # Decrease the indegree of all nodes that this node points to
        for k in range(cols):
            if AMat[j, k] == 1:
                indegree[k] -= 1
    
    return toposortlist

# Example usage:
AMat = np.array([
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
])

print(toposort(AMat))

```

    [0, 1, 2, 3, 4]



```python
from queue import Queue

def toposortlist(AList):
    """
    Performs a topological sort on a directed acyclic graph (DAG) using Kahn's algorithm.
    
    Parameters:
    AList (dict): Adjacency list representing the graph, where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
    list: A list of nodes in topologically sorted order.
    """
    
    # Initialize the indegree dictionary and the list to store the topological sort result
    indegree = {}
    toposortlist = []

    # Step 1: Initialize all nodes' indegree to 0
    for u in AList.keys():
        indegree[u] = 0
    
    # Step 2: Compute indegree for each node
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v] + 1
    
    # Step 3: Initialize the queue with nodes having zero indegree
    zerodegreeq = Queue()
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.put(u)
    
    # Step 4: Perform the topological sort
    while not zerodegreeq.empty():
        # Dequeue a node with zero indegree
        j = zerodegreeq.get()
        # Append it to the topological sort list
        toposortlist.append(j)
        
        # Decrease the indegree of all its adjacent nodes
        for k in AList[j]:
            indegree[k] = indegree[k] - 1
            # If the indegree of any adjacent node becomes zero, enqueue it
            if indegree[k] == 0:
                zerodegreeq.put(k)
    
    return toposortlist

# Example usage:
AList = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

# Prints the topological sort of the graph
print(toposortlist(AList))


```

    ['A', 'B', 'C', 'D', 'E']



```python

```
