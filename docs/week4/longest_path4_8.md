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

    time taken:2.27989999075362e-05



```python
from queue import Queue

def longestpathlist(AList):
    """
    Computes the longest path in a directed acyclic graph (DAG) using an adjacency list.

    Parameters:
    AList (dict): Adjacency list representing the graph, where keys are nodes and values are lists of adjacent nodes.

    Returns:
    dict: A dictionary where keys are nodes and values are the lengths of the longest paths ending at those nodes.
    """

    # Initialize indegree and longest path length dictionaries
    indegree = {}
    lpath = {}
    for u in AList.keys():
        indegree[u] = 0
        lpath[u] = 0

    # Compute indegree for each node
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] += 1

    # Initialize the zero degree queue
    zerodegreeq = Queue()
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.put(u)

    # Process nodes with zero indegree
    while not zerodegreeq.empty():
        j = zerodegreeq.get()

        for k in AList[j]:
            indegree[k] -= 1
            lpath[k] = max(lpath[k], lpath[j] + 1)
            if indegree[k] == 0:
                zerodegreeq.put(k)

    return lpath

# Example usage:
AList = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

# Prints the longest path lengths from each node
print(longestpathlist(AList))

```

    {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 3}



```python

```
