# Lecture 6.5 - Search Trees.pdf (PDF file)
**Summary**
## Search Trees

### Dynamic Sorted Data

Dynamic sorted data is essential for efficient searching, especially when data changes dynamically with items being periodically inserted and deleted. Inserting or deleting an item from a sorted list takes O(n) time.

### Binary Search Tree

A binary search tree (BST) is a tree data structure that maintains the property that all values in the left subtree of a node are less than the node's value, and all values in the right subtree are greater than the node's value.

#### Implementing a Binary Search Tree

Each node in a BST has a value and pointers to its children. To simplify implementation, an empty frontier is added with empty nodes filled with None values. The empty tree is a single empty node. Leaf nodes point to empty nodes. Implementing operations recursively becomes easier with this setup.

#### Inorder Traversal

Inorder traversal lists the values in a BST in sorted order by first listing the values in the left subtree, then the current node, and finally the values in the right subtree.

#### Find a Value

To find a value in a BST, start from the root node and compare the search value to the current node's value. If the search value is smaller, search the left subtree; if larger, search the right subtree. This process continues until the search value is found or the end of the tree is reached.

#### Minimum and Maximum

The minimum value in a BST is found in the leftmost node, and the maximum value is found in the rightmost node.

#### Insert a Value

To insert a new value into a BST, first attempt to find it. If not found, insert it at the position where the search fails.

#### Delete a Value

Deleting a value from a BST is more complex than insertion. If the value is not found, nothing is done. If the value is found in a leaf node, the node is simply made empty. If the value is found in a node with one child, the child is promoted to replace the node. If the value is found in a node with two children, the value is replaced with the maximum value of the left subtree, and that value is deleted from the left subtree.

### Complexity

The find(), insert(), and delete() operations in a BST all walk down a single path, resulting in a worst-case complexity of O(height of the tree). In an unbalanced tree with n nodes, the height can be O(n), leading to inefficient operations.

However, balanced trees have a height of O(log n), ensuring that all operations remain efficient. Techniques for maintaining a balanced tree will be explored to guarantee O(log n) complexity for all operations.
