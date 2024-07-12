# Lecture 6.3 - Heaps.pdf (PDF file)
**Summary**
**Heaps**

**Introduction**

Heaps are a type of tree data structure that can be used to implement priority queues. A priority queue is a data structure that allows us to store and retrieve elements based on their priority. The element with the highest priority is always retrieved first.

**Binary Trees**

Heaps are implemented using binary trees. A binary tree is a tree data structure in which each node has at most two children. The left child is typically referred to as the left subtree, and the right child is referred to as the right subtree.

**Heap Property**

Heaps are binary trees that satisfy the heap property. The heap property states that the value of each node is greater than or equal to the value of its children. This property ensures that the element with the highest priority is always at the root of the heap.

**Types of Heaps**

There are two types of heaps:

* **Max-heap:** In a max-heap, the value of each node is greater than or equal to the value of its children.
* **Min-heap:** In a min-heap, the value of each node is less than or equal to the value of its children.

**Heap Operations**

The following are the основни operations that can be performed on heaps:

* **Insert:** Inserts a new element into the heap.
* **Delete:** Deletes the element with the highest priority from the heap.
* **Heapify:** Builds a heap from an unsorted array.

**Complexity of Heap Operations**

The complexity of the heap operations is as follows:

* **Insert:** O(log N)
* **Delete:** O(log N)
* **Heapify:** O(N)

**Applications of Heaps**

Heaps can be used to solve a wide variety of problems, including:

* **Priority queues:** Heaps can be used to implement priority queues, which are used to store and retrieve elements based on their priority.
* **Sorting:** Heaps can be used to sort an array of elements in O(N log N) time.
* **Selection:** Heaps can be used to find the kth largest element in an array in O(N log k) time.
* **Median:** Heaps can be used to find the median of a set of numbers in O(N) time.

**Implementation**

Heaps can be implemented using a variety of data structures, including arrays and linked lists. The following is a simple implementation of a max-heap using an array:

```
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        if len(self.heap) == 0:
            return None

        max_value = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self._heapify_down(0)

        return max_value

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

    def _heapify_down(self, index):
        while True:
            left_child_index = (index * 2) + 1
            right_child_index = (index * 2) + 2
            largest_index = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest_index]:
                largest_index = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest_index]:
                largest_index = right_child_index

            if largest_index == index:
                break

            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            index = largest_index
```
