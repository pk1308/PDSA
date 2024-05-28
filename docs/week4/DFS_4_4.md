```python
import os
import numpy as np

os.chdir("..")
os.chdir("..")
from driver_folder.time_driver import TimerError
```


```python
T = TimerError()
T.start()
end_time = T.elapsed()
print(f"time taken:{end_time}")
```

    time taken:1.3529000170819927e-05



```python
def DFSInitList(AList):
    """
    Initializes the visited and parent dictionaries for each node in the graph.

    Parameters:
        AList (dict): The adjacency list representation of the graph.

    Returns:
        tuple: A tuple containing two dictionaries:
               - visited: A dictionary to track visited nodes, initialized to False.
               - parent: A dictionary to track parent nodes, initialized to -1.
    """
    visited = {}
    parent = {}
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1
    return (visited, parent)


def DFSList(AList, visited, parent, v):
    """
    Performs Depth-First Search (DFS) traversal recursively starting from node v.

    Parameters:
        AList (dict): The adjacency list representation of the graph.
        visited (dict): A dictionary to track visited nodes.
        parent (dict): A dictionary to track parent nodes.
        v (hashable): The current node being visited.

    Returns:
        tuple: A tuple containing two dictionaries:
               - visited: Updated dictionary with visited nodes.
               - parent: Updated dictionary with parent nodes.
    """
    visited[v] = True
    for k in AList[v]:
        if not visited[k]:
            parent[k] = v
            DFSList(AList, visited, parent, k)
    return (visited, parent)


def DFSGlobal(AList, k):
    """
    Initializes DFS and starts DFS traversal from node k in the graph.

    Parameters:
        AList (dict): The adjacency list representation of the graph.
        k (hashable): The starting node for DFS traversal.

    Returns:
        tuple: A tuple containing two dictionaries:
               - visited: Dictionary with visited nodes after DFS traversal.
               - parent: Dictionary with parent nodes after DFS traversal.
    """
    (visited, parent) = DFSInitList(AList)
    (visited, parent) = DFSList(AList, visited, parent, k)
    return (visited, parent)


# Example usage:
AList = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

# Starting node
start_node = "A"
visited, parent = DFSGlobal(AList, start_node)
print("Visited nodes:", visited)
print("Parent nodes:", parent)
```

    Visited nodes: {'A': True, 'B': True, 'C': True, 'D': True, 'E': True, 'F': True}
    Parent nodes: {'A': -1, 'B': 'A', 'C': 'F', 'D': 'B', 'E': 'B', 'F': 'E'}



```python

```
