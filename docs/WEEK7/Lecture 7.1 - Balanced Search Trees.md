# Lecture 7.1 - Balanced Search Trees.pdf (PDF file)
**Summary**
**Balanced Search Trees**

**Introduction**

Search trees are data structures that efficiently store and search for data. They are implemented using nodes that contain a value and pointers to child nodes. Search trees allow for efficient find(), insert(), and delete() operations by traversing a single path from the root to the desired node. However, unbalanced search trees can have a height of O(n), resulting in poor performance for the find(), insert(), and delete() operations.

**Height Balanced Trees**

Balanced search trees maintain a height of O(log n), ensuring efficient operations. They achieve this by enforcing a height balance property, where the difference between the heights of the left and right subtrees of any node is at most 1.

**Slope of a Node**

The slope of a node is defined as the difference between the height of its left subtree and the height of its right subtree. A balanced tree has a slope of -1, 0, or 1 for all nodes.

**Correcting Imbalance**

Insert and delete operations can alter the slope of a node, potentially causing imbalance. To correct this, rotations are performed.

**Rotations**

* **Left Rotation:** Converts a slope of -2 to a slope of 0 or 1.
* **Right Rotation:** Converts a slope of 2 to a slope of -1, 0, or 1.

**Rebalancing**

When the root node of a tree has a slope of 2, rebalancing is performed. This involves:

* **Case 1:** If the slope of the left child is 0 or 1, perform a right rotation at the root.
* **Case 2:** If the slope of the left child is -1, perform a left rotation at the left child followed by a right rotation at the root.

**Updating Insert() and Delete()**

The insert() and delete() functions are updated to include rebalancing after each modification.

**Computing Slope**

To compute the slope, the height of each subtree must be known. Instead of computing height, which is O(n), a self.height field is maintained and updated after each modification.

**Summary**

* Rotations can maintain height balance in search trees.
* Height-balanced trees have O(log n) height.
* The find(), insert(), and delete() operations take O(log n) time in height-balanced trees.
