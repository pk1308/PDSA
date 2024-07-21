# Lecture 8.4 - Divide and Conquer-Recursion Trees.pdf (PDF file)
**Summary**
**Divide and Conquer: Recursion Trees**

In computer science, divide and conquer is a technique for solving a problem by recursively breaking it down into smaller subproblems that are easier to solve. Divide and conquer is an efficient way to solve problems that can be broken down into independent subproblems, such as sorting, searching, and finding the minimum or maximum element in a list.

**Recursion Trees**

A recursion tree is a rooted tree that represents the recursive calls made by a divide and conquer algorithm. The root of the tree represents the original problem, and the children of the root represent the subproblems that are created when the problem is divided. The leaves of the tree represent the base cases of the recursion, which are the cases where the problem is small enough to be solved directly.

The height of a recursion tree is the number of levels in the tree, and the width of a recursion tree is the maximum number of children that any node in the tree has. The size of a recursion tree is the total number of nodes in the tree.

**Asymptotic Analysis of Divide and Conquer Recurrences**

The asymptotic complexity of a divide and conquer algorithm can be determined by analyzing the size of the recursion tree. The following are three common cases:

* **Decreasing size:** If the size of the subproblems decreases by a constant factor at each level of the recursion tree, then the total size of the recursion tree is O(n), where n is the size of the original problem.
* **Equal size:** If the size of the subproblems is the same at each level of the recursion tree, then the total size of the recursion tree is O(n log n), where n is the size of the original problem.
* **Increasing size:** If the size of the subproblems increases by a constant factor at each level of the recursion tree, then the total size of the recursion tree is O(n^c), where c is the constant factor.

**Examples**

Here are a few examples of divide and conquer algorithms and their associated recursion trees:

* **Merge sort:** Merge sort is a sorting algorithm that divides the input array into two halves, sorts each half recursively, and then merges the sorted halves together. The recursion tree for merge sort is a binary tree, where each node represents a subarray of the input array. The height of the recursion tree is O(log n), where n is the size of the input array, and the width of the recursion tree is O(1). The total size of the recursion tree is O(n log n).
* **Quick sort:** Quick sort is a sorting algorithm that selects a pivot element from the input array, partitions the array into two subarrays based on the pivot element, and then recursively sorts each subarray. The recursion tree for quick sort is a binary tree, where each node represents a subarray of the input array. The height of the recursion tree is O(log n), where n is the size of the input array, and the width of the recursion tree is O(1). The total size of the recursion tree is O(n log n).
* **Binary search:** Binary search is a searching algorithm that repeatedly divides the input array in half until the target element is found. The recursion tree for binary search is a binary tree, where each node represents a subarray of the input array. The height of the recursion tree is O(log n), where n is the size of the input array, and the width of the recursion tree is O(1). The total size of the recursion tree is O(log n).

**Conclusion**

Recursion trees are a useful tool for understanding the asymptotic complexity of divide and conquer algorithms. By analyzing the size of the recursion tree, we can determine the worst-case running time of the algorithm.
