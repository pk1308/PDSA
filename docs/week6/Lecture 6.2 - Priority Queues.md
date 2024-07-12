# Lecture 6.2 - Priority Queues.pdf (PDF file)
**Summary**
**Priority Queues**

**Introduction**

A priority queue is a data structure that maintains a collection of elements, each with a priority. The operations on a priority queue are:

* insert(): Insert an element into the queue.
* delete max(): Remove and return the element with the highest priority from the queue.

**Applications**

Priority queues have a wide range of applications, including:

* Job scheduling: A job scheduler uses a priority queue to schedule jobs on a computer. The jobs with the highest priorities are scheduled first.
* Network routing: A network router uses a priority queue to route packets. The packets with the highest priorities are routed first.
* Event simulation: An event simulation uses a priority queue to simulate events. The events with the earliest time stamps are processed first.

**Implementing Priority Queues with One-Dimensional Structures**

One-dimensional structures, such as unsorted lists and sorted lists, can be used to implement priority queues. However, these implementations have limitations.

Unsorted lists have O(n) insert() and delete max() operations, where n is the number of elements in the list. Sorted lists have O(1) delete max() operations, but O(n) insert() operations.

**Moving to Two Dimensions**

An alternative approach to implementing priority queues is to use two-dimensional structures. One implementation is to maintain a √N × √N array, where each row is sorted in ascending order.

* insert(): Insert an element into the first row that has space.
* delete max(): Find the maximum element in the last column and delete it.

This implementation has O(√N) insert() and delete max() operations.

**Summary of Two-Dimensional Implementation**

* 2D √N × √N array with sorted rows
* insert() is O(√N)
* delete max() is O(√N)
* Processing N items is O(N√N)

**Can We Do Better?**

The two-dimensional implementation has a time complexity of O(√N) for insert() and delete max() operations. Can we do better?

**Heaps**

A heap is a special binary tree that satisfies the following properties:

* The key of a node is greater than or equal to the keys of its children.
* The tree is complete, meaning that all levels are full except possibly the last level, which is filled from left to right.

Heaps have the following performance characteristics:

* Height: O(log N)
* insert(): O(log N)
* delete max(): O(log N)

**Processing N Items with a Heap**

Using a heap to implement a priority queue, we can process N items in O(N log N) time. This is an improvement over the two-dimensional implementation, which takes O(N√N) time.

**Summary of Heap Implementation**

* Maintain a special binary tree — heap
* Height: O(log N)
* insert(): O(log N)
* delete max(): O(log N)
* Processing N items: O(N log N)
* Flexible — need not fix N in advance
