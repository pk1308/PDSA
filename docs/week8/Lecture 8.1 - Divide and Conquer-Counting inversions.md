# Lecture 8.1 - Divide and Conquer-Counting inversions.pdf (PDF file)
**Summary**
**Divide and Conquer: Counting Inversions**

**Introduction:**
Divide and conquer is a paradigm that breaks a problem into disjoint subproblems, solves each subproblem separately, and then combines these solutions efficiently. Examples of divide and conquer algorithms include merge sort and quicksort.

**Problem Statement: Counting Inversions**
In the context of recommender systems, one challenge is to measure the similarity between user rankings. One measure is the number of inversions in one ranking relative to another. An inversion occurs when a movie ranked higher in one list is ranked lower in the other. The number of inversions provides a measure of dissimilarity between the two rankings.

**Brute Force Approach:**
A brute force approach to counting inversions is to check every pair of elements in the two rankings, which requires O(n^2) time complexity.

**Divide and Conquer Approach:**
A more efficient approach is to use divide and conquer. The algorithm is as follows:

1. Divide the two rankings into two halves.
2. Recursively count the inversions in each half.
3. Count the inversions across the boundary between the two halves. This is done by merging the two halves while counting the number of inversions that occur when an element from the left half is greater than an element from the right half.

**Analysis:**
The recurrence relation for the divide and conquer algorithm is similar to that of merge sort:
```
T(n) = 2T(n/2) + n
```

Solving this recurrence relation using the Master Theorem shows that the time complexity of the algorithm is O(n log n). This is a significant improvement over the O(n^2) time complexity of the brute force approach.

**Python Implementation:**

```python
def merge_and_count(A, B):
    (m, n) = (len(A), len(B))
    (C, i, j, k, count) = ([], 0, 0, 0, 0)
    while k < m+n:
        if i == m:
            C.append(B[j])
            (j, k) = (j+1, k+1)
        elif j == n:
            C.append(A[i])
            (i, k) = (i+1, k+1)
        elif A[i] < B[j]:
            C.append(A[i])
            (i, k) = (i+1, k+1)
        else:
            C.append(B[j])
            (j, k, count) = (j+1, k+1, count+(m-i))
    return(C, count)

def sort_and_count(A):
    n = len(A)
    if n <= 1:
        return(A, 0)
    (L, countL) = sort_and_count(A[:n//2])
    (R, countR) = sort_and_count(A[n//2:])
    (B, countB) = merge_and_count(L, R)
    return(B, countL+countR+countB)
```

**Conclusion:**
The divide and conquer approach to counting inversions provides a significant improvement in efficiency compared to the brute force approach. It has a time complexity of O(n log n) and is suitable for large datasets. This algorithm can be applied in various contexts, including recommender systems and data analysis.
