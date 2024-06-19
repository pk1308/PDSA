# Lecture 4.8 - Longest Path in DAGs.pdf (PDF file)
**Summary**
## Longest Paths in DAGs

Directed acyclic graphs (DAGs) are a special type of graph that does not contain any cycles. This makes them a natural way to representdependencies, such as in a prerequisite graph or a job dependency graph.

One important problem that arises in the context of DAGs is finding the longest path from a given source vertex to a given destination vertex. The longest path problem can be used to determine the minimum number of steps required to complete a task, or the longest possible sequence of events that can occur in a system.

**Topological sorting** is an algorithm that can be used to find a linear ordering of the vertices in a DAG. This ordering is such that, for any edge (u, v) in the DAG, u comes before v in the ordering. Topological sorting can be used to find the longest path in a DAG by starting at the source vertex and following the edges in the topological order. The longest path will be the path that ends at the destination vertex.

The following pseudocode implements a topological sort algorithm:

```
def topological_sort(G):
  """
  Perform topological sort on a DAG.

  Args:
    G: A DAG.

  Returns:
    A list of vertices in topological order.
  """

  # Initialize a stack to store the vertices.
  stack = []

  # Initialize a set to store the visited vertices.
  visited = set()

  # Iterate over the vertices in the graph.
  for v in G.vertices:
    # If the vertex has not been visited, perform a topological sort on it.
    if v not in visited:
      topological_sort_helper(v, stack, visited)

  # Return the stack.
  return stack


def topological_sort_helper(v, stack, visited):
  """
  Helper function for topological sort.

  Args:
    v: The vertex to perform topological sort on.
    stack: The stack to store the vertices.
    visited: The set to store the visited vertices.
  """

  # Mark the vertex as visited.
  visited.add(v)

  # Iterate over the edges in the graph.
  for (v, w) in G.edges:
    # If the edge has not been visited, perform a topological sort on it.
    if (v, w) not in visited:
      topological_sort_helper(w, stack, visited)

  # Push the vertex onto the stack.
  stack.append(v)
```

Once the topological sort has been performed, the longest path can be found by starting at the source vertex and following the edges in the topological order. The longest path will be the path that ends at the destination vertex.

The following pseudocode implements an algorithm to find the longest path in a DAG:

```
def longest_path(G, source, destination):
  """
  Find the longest path from a source vertex to a destination vertex in a DAG.

  Args:
    G: A DAG.
    source: The source vertex.
    destination: The destination vertex.

  Returns:
    The length of the longest path.
  """

  # Perform topological sort on the graph.
  topological_order = topological_sort(G)

  # Initialize a dictionary to store the longest paths.
  longest_paths = {}

  # Iterate over the vertices in the topological order.
  for v in topological_order:
    # If the vertex is the source vertex, set the longest path to 0.
    if v == source:
      longest_paths[v] = 0

    # Otherwise, iterate over the edges in the graph.
    else:
      longest_paths[v] = max([longest_paths[u] + 1 for (u, v) in G.edges if u in longest_paths])

  # Return the longest path to the destination vertex.
  return longest_paths[destination]
```

The time complexity of the longest path algorithm is O(m + n), where m is the number of edges in the DAG and n is the number of vertices in the DAG.

## Applications of Longest Paths in DAGs

The longest path problem has a number of applications in computer science. Some of these applications include:

* **Scheduling:** The longest path problem can be used to find the minimum number of steps required to complete a task. This can be used to schedule tasks in a way that minimizes the overall completion time.
* **Job dependency:** The longest path problem can be used to find the longest possible sequence of events that can occur in a system. This can be used to identify potential bottlenecks in the system and to improve the system's performance.
* **Critical path analysis:** The longest path problem can be used to find the critical path in a project. The critical path is the sequence of tasks that must be completed on time in order for the project to be completed on time.

## Conclusion

The longest path problem is a fundamental problem in computer science. It has a number of applications in scheduling, job dependency, and critical path analysis. There are a number of algorithms that can be used to solve the longest path problem, including the topological sort algorithm and the longest path algorithm.
