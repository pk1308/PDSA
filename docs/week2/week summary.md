```python
import sys

sys.setrecursionlimit(2**31 - 1)
```


```python
import sys
from loguru import logger as lg
import random
import time


class TimerError(Exception):
    def __init__(self) -> None:
        self._start_time = None
        self._stop_time = None
        self.elapsed_time = None

    def start(self):
        if self._start_time != None:
            raise TimerError(" please stop the timer")
        self._start_time = time.perf_counter()
        self._stop_time = None

    def stop(self):
        if self._start_time == None:
            raise TimerError("please start the timer")
        self._stop_time = time.perf_counter()
        self.elapsed_time = self._stop_time - self._start_time
        self._start_time = None

    def elapsed(self):
        if self.elapsed == None and self._start_time == None:
            raise TimerError("the counter not running")
        else:
            self.stop()
            return self.elapsed_time

    def __str__(self) -> str:
        return str(self.elapsed_time)


T = TimerError()
T.start()
end_time = T.elapsed()
lg.info(f"time taken:{end_time}")
```

    [32m2024-05-08 23:58:37.997[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m38[0m - [1mtime taken:1.1069001629948616e-05[0m



```python
random.seed(1965)
```


```python
L = [random.randint(1, 1000000000) for i in range(10000)]
```


```python
v = random.randint(1, 1000000)
```

# Naive Approach 


```python
def naive_search(V, L):
    for x in L:
        if V == x:
            return True
    else:
        return False
```

complexity = O(n)

# binary search 

# sorting function 


```python
def sort_list(L: list):
    if len(L) == 0:
        return []
    midpoint = len(L) // 2
    mid_value = L[midpoint]
    lower_list = [low for low in L if low < mid_value]
    mid_list = [mid for mid in L if mid == mid_value]
    upper_list = [upper for upper in L if upper > mid_value]
    return sort_list(lower_list) + mid_list + sort_list(upper_list)
```


```python
midpoint = len(L) // 2
mid_value = L[midpoint]
```


```python
T = TimerError()
T.start()
print(f"length of L :{len(L)}")
sort_list(L)
end_time = T.elapsed()
lg.info(f"time taken:{end_time}")
```

    [32m2024-05-08 23:58:38.066[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime taken:0.011552168987691402[0m


    length of L :10000



```python
def sort_list(L: list) -> list:
    """Sorts a list of numbers in ascending order using Quicksort algorithm.

    Args:
        L: The list to be sorted.

    Returns:
        A new list containing the sorted elements of the original list.
    """

    if len(L) <= 1:
        return L

    midpoint = len(L) // 2
    mid_value = L[midpoint]
    lower_list = sort_list([low for low in L if low < mid_value])
    upper_list = sort_list([upper for upper in L if upper > mid_value])
    mid_list = [mid for mid in L if mid == mid_value]
    return lower_list + mid_list + upper_list
```


```python
T = TimerError()
T.start()
print(f"length of L :{len(L)}")
L = sort_list(L)
end_time = T.elapsed()
lg.info(f"time taken:{end_time}")
```

    [32m2024-05-08 23:58:38.093[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime taken:0.01215230894740671[0m


    length of L :10000



```python
def binarysearch(v: int, L: list) -> bool:

    if not L:
        return False
    midpoint = len(L) // 2

    if v == L[midpoint]:
        return True
    if v < L[midpoint]:
        return binarysearch(v, L[:midpoint])
    else:
        return binarysearch(v, L[midpoint + 1 :])
```

Complexity = O(logn)


```python
T = TimerError()
T.start()
print(f"length of L :{len(L)}")
end_time = T.elapsed()
lg.info(f"time taken naive :{end_time}")
```

    [32m2024-05-08 23:58:38.106[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m5[0m - [1mtime taken naive :0.0001515159965492785[0m


    length of L :10000



```python
T = TimerError()
T.start()
print(f"length of L :{len(L)}")
print(binarysearch(v, L))
end_time = T.elapsed()
lg.info(f"time taken binary:{end_time}")
```

    [32m2024-05-08 23:58:38.112[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime taken binary:0.0001189609756693244[0m


    length of L :10000
    False



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


T = TimerError()
T.start()
SelectionSort(L)
end_time_1 = T.elapsed()
lg.info(f"time taken SelectionSort:{end_time_1}")


def sort_list(L: list):
    if len(L) == 0:
        return []
    midpoint = len(L) // 2
    mid_value = L[midpoint]
    lower_list = [low for low in L if low < mid_value]
    mid_list = [mid for mid in L if mid == mid_value]
    upper_list = [upper for upper in L if upper > mid_value]
    return sort_list(lower_list) + mid_list + sort_list(upper_list)


T = TimerError()
T.start()
sort_list(L)
end_time_2 = T.elapsed()
lg.info(f"time taken sort_list:{end_time_2}")
```

    [32m2024-05-08 23:58:38.914[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m21[0m - [1mtime taken SelectionSort:0.7941872259834781[0m
    [32m2024-05-08 23:58:38.922[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m35[0m - [1mtime taken sort_list:0.007573203009087592[0m



```python
# insertion sort
def insertion_sort(L):
    """
    Sorts a list using the insertion sort algorithm.

    Args:
        L (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(L)

    # If the list has 1 or fewer elements, it is already sorted
    if n <= 1:
        return L

    # Iterate through each element in the list
    for i in range(n):
        j = i

        # Mo value_to_inserte the element at index j towards the beginning of the list
        # until it's in the correct sorted position
        while j > 0 and L[j] < L[j - 1]:
            # Swap the current element with the prevalue_to_insertalue_to_insertious one if it's smaller
            L[j], L[j - 1] = L[j - 1], L[j]
            j -= (
                1  # Decrement j to movalue_to_inserte towards the beginning of the list
            )

    return L


T = TimerError()
T.start()
insertion_sort(L)
end_time = T.elapsed()
lg.info(f"time taken insertion_sort:{end_time}")


def Insert(List_to_sort, Value_to_insert):
    """
    Inserts a value into a sorted list while maintaining the sorted order.

    Args:
        List_to_sort (list): The sorted list to insert the value into.
        Value_to_insert (Any): The value to insert into the list.

    Returns:
        list: The sorted list after inserting the value.
    """
    n = len(List_to_sort)

    # If the list is empty, simply return the value as a single-element list
    if n == 0:
        return [Value_to_insert]

    # If the value is greater than or equal to the last element in the list,
    # append it to the end of the list
    if Value_to_insert >= List_to_sort[-1]:
        return List_to_sort + [Value_to_insert]
    else:
        # Recursively insert the value into the sublist List_to_sort[:-1]
        # and then append the last element of List_to_sort to the result
        return Insert(List_to_sort[:-1], Value_to_insert) + List_to_sort[-1:]


def ISort(List_to_sort):
    """
    Sorts a list using the insertion sort algorithm recursively.

    Args:
        List_to_sort (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(List_to_sort)

    # If the list has less than 1 element, it is already sorted
    if n < 1:
        return List_to_sort

    # Recursively sort the sublist List_to_sort[:-1]
    # and then insert the last element of List_to_sort into the sorted sublist
    L = Insert(ISort(List_to_sort[:-1]), List_to_sort[-1])

    return L


T = TimerError()
T.start()
ISort(L)
end_time = T.elapsed()
lg.info(f"time taken merge Sort(:{end_time}")
```

    [32m2024-05-08 23:58:38.929[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m35[0m - [1mtime taken insertion_sort:0.0003439149586483836[0m
    [32m2024-05-08 23:58:39.333[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m89[0m - [1mtime taken merge Sort(:0.40309521002927795[0m



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


T = TimerError()
T.start()
mergesort(L)
end_time = T.elapsed()
lg.info(f"time taken merge sort :{end_time}")
```

    [32m2024-05-08 23:58:39.347[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m64[0m - [1mtime taken merge sort :0.006971621012780815[0m



```python
T = TimerError()
T.start()

mergesort(list(range(1000000, 0, -1)))
end_time = T.elapsed()
lg.info(f"time taken merge sort :{end_time}")
```

    [32m2024-05-08 23:58:40.284[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime taken merge sort :0.9263360829791054[0m



```python
T = TimerError()
T.start()

mergesort(list(range(1000000)))
end_time = T.elapsed()
lg.info(f"time taken merge sort :{end_time}")
```

    [32m2024-05-08 23:58:41.205[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime taken merge sort :0.9164764899760485[0m



```python
L = [random.randint(1, 1000000) for i in range(1000000)]
T = TimerError()
T.start()
mergesort(L)
end_time = T.elapsed()
lg.info(f"time taken merge sort :{end_time}")
```

    [32m2024-05-08 23:59:49.059[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime taken merge sort :1.6022985609597526[0m



```python

```
