What are the three main types of complexity cases we consider when analyzing algorithms?

- space complexity -   the ram spaced used in excuting the program
- time complexity - the time taken for the code
- storage complexity - the space used to store the code

Explain the difference between Big-O, Omega, and Theta notations in complexity analysis.

- BIg - O is the worst case scenario or upper bound
- Omega $ \omega$ = average case scenario or tight bound
- Theta $\theta$ = best case scenario

What is the time complexity of binary search? Explain why it has this complexity.

- binary search is the list is sorted  $ (log(n))$ = if the list is sorted we can access the mid point using then len of the list / 2 and we will be able to point out if the element we are searching is on the right or left of the mid point and we can change the left or right index recurisly 

```python
def binarysearch(v: int, L: list) -> bool:
	# n = 100 
    if not L:

        return False
    midpoint = len(L) // 2  # n^2 

    if v == L[midpoint]: 
        return True
    if v < L[midpoint]:
        return binarysearch(v, L[:midpoint])
    else:
        return binarysearch(v, L[midpoint + 1 :]) #  L[51:75]
```


Describe the selection sort algorithm and give its time complexity.

Time complexity = $O(n^{2})$

we select an elememt compare with the rest of the elements and switch position based bigger or smaller 

the complexity always n^2

stable sort = selection sort is not stable bescause for eg we have a list [ 4_a , 3 , 4_b , 1]  in selection sort the end result in will be 

[  3 , 4_b , 1, 4_a]

inplace =  yes 

as we compare all elements twice we will have n^2 

How does insertion sort work? In what scenario would insertion sort perform better than other sorting algorithms?

best  = $O(n)$ this is went the elements already sorted 

average  = $o(n^2)$ = when the list is simlar to [1,3,2,4]

worst  = $o(n^2)$ = when the lis is in descending order 

inplace = yes 

stable = yes 


```python
def SelectionSort(L):
    n = len(L)
    if n <= 1:
        return L
    for i in range(n):
        # Assume L[:i] is sorted
        mpos = i
        # mpos: position of minimum in L[i:]
        for j in range(i + 1, n):
            if L[j] < L[mpos]:
                mpos = j
                # L[mpos] : smallest value in L[i:]
                # # Exchange L[mpos] and L[i]
                (L[i], L[mpos]) = (L[mpos], L[i])
                # Now L[:i+1] is sorted
                return L
```

Explain the merge sort algorithm. Why is it considered more efficient than selection and insertion sort for large datasets?

best , worst ,  average = $n(log(n))$

```python


def merge(A, B):
    """
    Merge two sorted lists A and B into a single sorted list.

    Args:
        A (list): The first sorted list.
        B (list): The second sorted list.

    Returns:
        list: The merged sorted list.
    """
    C, i, j, k = [], 0, 0, 0
    m, n = len(A), len(B)

    while k < m + n:
        if i == m:
            C.extend(B[j:])
            k = k + (n - j)
        elif j == n:
            C.extend(A[i:])
            k = k + (m - i)
        elif A[i] < B[j]:
            C.append(A[i])
            i, k = i + 1, k + 1
        else:
            C.append(B[j])
            j, k = j + 1, k + 1

    return C


def mergesort(A):
    """
    Sorts a list using the merge sort algorithm.

    Args:
        A (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(A)

    # Base case: If the list has 0 or 1 element, it is already sorted
    if n <= 1:
        return A

    # Recursively split the list into two halves and sort each half
    L = mergesort(A[: n // 2])
    R = mergesort(A[n // 2 :])

    # Merge the sorted halves
    B = merge(L, R)

    return B
```

no matter if the order of the element merge sort will always take n(logn) 



What is the difference between a stable and unstable sorting algorithm? Which of the sorting algorithms we've discussed are stable?

in stable sort the the order of occurance is maintained for example insertionsort and eg of un stable selection sort 

Give an example of a scenario where the time complexity of an algorithm would be O(n^3).


An example of a scenario where the time complexity of an algorithm would be \( O(n^3) \) is the multiplication of two \( n \times n \) matrices using the naive matrix multiplication algorithm.

In this algorithm, the multiplication of two matrices \( A \) and \( B \) to produce a matrix \( C \) is performed as follows:

1. Initialize matrix \( C \) with all zeros.
2. For each element \( C[i][j] \) in the result matrix \( C \):
   - Compute the sum of the products of corresponding elements from row \( i \) of matrix \( A \) and column \( j \) of matrix \( B \):
     \[
     C[i][j] = \sum_{k=0}^{n-1} A[i][k] \cdot B[k][j]
     \]

To break this down:

- There are \( n^2 \) elements in the resulting matrix \( C \), since it is also an \( n \times n \) matrix.
- For each element \( C[i][j] \), there is an inner loop that runs \( n \) times to compute the sum of the products.

Therefore, the total number of operations is \( n \) (outer loop) times \( n \) (inner loop for each row) times \( n \) (inner loop for each column), resulting in \( n \times n \times n = n^3 \) operations.

Thus, the naive matrix multiplication algorithm has a time complexity of \( O(n^3) \).

What is the space complexity of merge sort? Why?

the space comlecity in o(n) as it recursive called after dividing the input to two 

Compare the best-case time complexities of insertion sort and merge sort.

the best is when the list is sorted = in this case insertion sort will take o(n) and merge sort will take n(logn)
