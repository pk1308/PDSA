# Lecture 8.5 - Divide and Conquer-Quick Select.pdf (PDF file)
**Summary**
**Divide and Conquer: Quick Select**

**Introduction**

Quick Select is an efficient algorithm that finds the k-th largest element in a list or array. It is based on the principle of divide and conquer.

**Divide and Conquer Approach**

The divide and conquer approach involves the following steps:

1. **Division:** Divide the list into two sublists: a lower sublist containing elements less than a pivot value and an upper sublist containing elements greater than or equal to the pivot value.
2. **Conquer:** Recursively apply the divide and conquer approach to the lower and upper sublists to find the k-th largest element in each sublist.
3. **Combine:** Determine the k-th largest element in the original list based on the results from the sublists.

**Partitioning into Lower and Upper Sublists**

Partitioning is a key step in Quick Select. For a given pivot value, the list is partitioned into two sublists as follows:

* **Lower Sublist:** Contains all elements less than the pivot value.
* **Upper Sublist:** Contains all elements greater than or equal to the pivot value.

**Pivot Selection**

The choice of pivot is crucial for the efficiency of Quick Select. A good pivot is one that divides the list into roughly equal halves.

**Worst-Case Complexity**

In the worst case, Quick Select has a time complexity of O(n^2), similar to the worst-case complexity of quicksort. This occurs when the pivot selection is poor, resulting in extremely unbalanced sublists.

**Median of Medians**

To improve the worst-case complexity, the median of medians algorithm is used to select the pivot. This algorithm involves the following steps:

* Divide the list into blocks of 5 elements.
* Find the median of each block.
* Recursively apply the process to the list of block medians.

The median of the block medians is chosen as the pivot. This approach ensures that the pivot is close to the median of the list, resulting in a more balanced division.

**Analysis**

With the median of medians pivot selection, Quick Select has an average-case complexity of O(n). This is a significant improvement over the worst-case complexity of O(n^2).

**Summary**

Quick Select is a divide and conquer algorithm that efficiently finds the k-th largest element in a list or array. The use of the median of medians pivot selection improves the worst-case complexity and makes the algorithm more efficient on average.

**Historical Note**

Quick Select was first described by C.A.R. Hoare in 1962, in the same paper that introduced quicksort. The median of medians algorithm was developed in 1973 by Manuel Blum, Robert Floyd, Vaughn Pratt, Ron Rivest, and Robert Tarjan.
