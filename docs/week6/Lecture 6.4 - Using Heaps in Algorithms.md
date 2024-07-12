# Lecture 6.4 - Using Heaps in Algorithms.pdf (PDF file)
**Summary**
**Heaps in Algorithms**

**Priority Queues and Heaps**

Priority queues support the following operations:

* insert()
* delete max() or delete min()

Heaps are a tree-based implementation of priority queues.

* insert(), delete max()/delete min() are both O(log n)
* heapify() builds a heap from a list/array in time O(n)
* Heap can be represented as a list/array
* Simple index arithmetic to find parent and children of a node

To use a heap in an algorithm, we need:

* A way to locate the node to update
* A way to update the value of a node

**Updating Values in a Min-Heap**

* Updating a value in a min-heap takes O(log n).
* Two additional dictionaries map vertices to heap positions and vice versa.
* Update VtoH and HtoV each time we swap values in the heap.

**Dijkstra's Algorithm**

Using Min-Heaps:

* Identifying the next vertex to visit is O(log n).
* Updating distance takes O(log n) per neighbor.
* Overall complexity: O((m+n) log n)

**Heap Sort**

* Start with an unordered list.
* Build a heap — O(n).
* Call delete max() n times to extract elements in descending order — O(n log n).
* After each delete max(), the heap shrinks by 1.
* Store the maximum value at the end of the current heap.
* In-place O(n log n) sort.

**Summary**

* Updating a value in a heap takes O(log n).
* Need to maintain additional pointers to map values to heap positions and vice versa.
* With this extended notion of heap, Dijkstra's algorithm complexity improves from O(n^2) to O((m+n) log n).
* In a similar way, improve Prim's algorithm to O((m+n) log n).
* Heaps can also be used to sort a list in place in O(n log n).
