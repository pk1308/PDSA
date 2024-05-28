# Lists and arrays

### Setup
- Set recursion limit to `maxint`, $2^{31}-1$
    - This is the highest value Python allows
- Set up `Timer` class to time executions




```python
import sys

sys.setrecursionlimit(2**31 - 1)
```


```python
import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None
        self._elapsed_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop()")
        self._start_time = time.perf_counter()

    def stop(self):
        """Save the elapsed time and re-initialize timer"""
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start()")
        self._elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

    def elapsed(self):
        """Report elapsed time"""
        if self._elapsed_time is None:
            raise TimerError("Timer has not been run yet. Use .start()")
        return self._elapsed_time

    def __str__(self):
        """print() prints elapsed time"""
        return str(self._elapsed_time)
```

### Python lists


```python
t = Timer()
t.start()
l = []
for i in range(10000000):
    l.append(i)
t.stop()
print(t)
```

    1.5493727650000437



```python
t = Timer()
t.start()
l = []
for i in range(300000):
    l.insert(0, i)
t.stop()
print(t)
```

    22.904139766999833


## Searching
### Naive search and binary search with lists


```python
def naivesearchlist(v, L):
    for x in L:
        if v == x:
            return True
    return False
```


```python
def binarysearchlist(v, L):
    if L == []:
        return False

    m = len(L) // 2

    if v == L[m]:
        return True

    if v < L[m]:
        return binarysearchlist(v, L[:m])
    else:
        return binarysearchlist(v, L[m + 1 :])
```

### Naive search and binary search with arrays


```python
def naivesearcharray(v, A, l, r):  # Search A[l:r]
    for i in range(l, r):
        if v == A[i]:
            return True
    return False
```


```python
def binarysearcharray(v, A, l, r):  # Search A[l:r]
    if r - l <= 0:
        return False

    m = (l + r) // 2

    if v == A[m]:
        return True

    if v < A[m]:
        return binarysearcharray(v, A, l, m)
    else:
        return binarysearcharray(v, A, m + 1, r)
```

### Performance comparison across $10^4$ worst case searches in a sequence of size $10^5$
- Looking for odd numbers in a sequence of even numbers

#### Naive search vs binary search on lists


```python
l = list(range(0, 100000, 2))
t = Timer()
t.start()
for i in range(3001, 13000, 2):
    v = naivesearchlist(i, l)
t.stop()
print()
print("Naive search", t)
t.start()
for i in range(3001, 13000, 2):
    v = binarysearchlist(i, l)
t.stop()
print()
print("Binary search", t)
```

    
    Naive search 10.573194997000428
    
    Binary search 0.8486883160003345


#### Naive search vs binary search on arrays


```python
import numpy as np

myarray = np.arange(0, 100000, 2)
t = Timer()
t.start()
for i in range(3001, 5000, 2):
    v = naivesearcharray(i, myarray, 0, np.prod(myarray.shape))
t.stop()
print()
print("Naive search", t)
t.start()
for i in range(3001, 13000, 2):
    v = binarysearcharray(i, myarray, 0, np.prod(myarray.shape))
t.stop()
print()
print("Binary search", t)
```

    
    Naive search 18.446638938000433
    
    Binary search 0.19533542499993928


### *Questions*
- Binary search in arrays is much faster than in lists
- Why is naive search in arrays slower than in lists?

## Sorting
### Selection sort

#### Selection sort on a list


```python
def SelectionSortList(L):
    n = len(L)
    if n < 1:
        return L
    for i in range(n):
        # Assume L[:i] is sorted
        mpos = i
        # mpos is position of minimum in L[i:]
        for j in range(i + 1, n):
            if L[j] < L[mpos]:
                mpos = j
        # L[mpos] is the smallest value in L[i:]
        (L[i], L[mpos]) = (L[mpos], L[i])
        # Now L[:i+1] is sorted
    return L
```

#### Selection sort on an array


```python
def SelectionSortArray(A):
    n = np.prod(A.shape)
    if n < 1:
        return A
    for i in range(n):
        # Assume A[:i] is sorted
        mpos = i
        # mpos is position of minimum in A[i:]
        for j in range(i + 1, n):
            if A[j] < A[mpos]:
                mpos = j
        # A[mpos] is the smallest value in A[i:]
        (A[i], A[mpos]) = (A[mpos], A[i])
        # Now A[:i+1] is sorted
    return A
```

### Selection sort performance is more or less the same for all inputs

#### Selection sort performance on lists


```python
import random

random.seed(2021)
inputlists = {}
inputlists["random"] = [random.randrange(100000) for i in range(10000)]
inputlists["ascending"] = [i for i in range(10000)]
inputlists["descending"] = [i for i in range(9999, -1, -1)]
t = Timer()
for k in inputlists.keys():
    tmplist = inputlists[k][:]
    t.start()
    SelectionSortList(tmplist)
    t.stop()
    print(k, t)
```

    random 5.009827684999436
    ascending 4.9249246090003
    descending 5.207206533999852


#### Selection sort performance on arrays


```python
import numpy as np
import random

random.seed(2021)
inputarrays = {}
inputarrays["random"] = np.arange(10000)
for i in range(10000):
    inputarrays["random"][i] = random.randrange(100000)
inputarrays["ascending"] = np.arange(10000)
inputarrays["descending"] = np.arange(9999, -1, -1)
t = Timer()
for k in inputarrays.keys():
    tmparray = inputarrays[k][:]
    t.start()
    SelectionSortArray(tmparray)
    t.stop()
    print(k, t)
```

    random 16.26913504999993
    ascending 16.298071097000502
    descending 16.776301769999918


### *Question:* Why is selection sort slower on arrays than on lists?

### Insertion sort, iterative, on lists


```python
def InsertionSortList(L):
    n = len(L)
    if n < 1:
        return L
    for i in range(n):
        # Assume L[:i] is sorted
        # Move L[i] to correct position in L[:i]
        j = i
        while j > 0 and L[j] < L[j - 1]:
            (L[j], L[j - 1]) = (L[j - 1], L[j])
            j = j - 1
        # Now L[:i+1] is sorted
    return L
```

### Insertion sort, iterative, on arrays


```python
def InsertionSortArray(A):
    n = np.prod(A.shape)
    if n < 1:
        return A
    for i in range(n):
        # Assume A[:i] is sorted
        # Move A[i] to correct position in A[:i]
        j = i
        while j > 0 and A[j] < A[j - 1]:
            (A[j], A[j - 1]) = (A[j - 1], A[j])
            j = j - 1
        # Now A[:i+1] is sorted
    return A
```

### Insertion sort preformance
- On already sorted input, performance is very good
- On reverse sorted input, performance is worse than selection sort

#### Insertion sort performance on lists


```python
import random

random.seed(2021)
inputlists = {}
inputlists["random"] = [random.randrange(100000) for i in range(10000)]
inputlists["ascending"] = [i for i in range(10000)]
inputlists["descending"] = [i for i in range(9999, -1, -1)]
t = Timer()
for k in inputlists.keys():
    tmplist = inputlists[k][:]
    t.start()
    InsertionSortList(tmplist)
    t.stop()
    print(k, t)
```

    random 9.761906529999976
    ascending 0.0018216439999605427


#### Insertion sort performance on arrays


```python
import numpy as np
import random

random.seed(2021)
inputarrays = {}
inputarrays["random"] = np.arange(10000)
for i in range(10000):
    inputarrays["random"][i] = random.randrange(100000)
inputarrays["ascending"] = np.arange(10000)
inputarrays["descending"] = np.arange(9999, -1, -1)
t = Timer()
for k in inputarrays.keys():
    tmparray = inputarrays[k][:]
    t.start()
    InsertionSortArray(tmparray)
    t.stop()
    print(k, t)
```

    random 22.89952142300001
    ascending 0.004247436000014204
    descending 46.23875934999995


### *Question:* Why is insertion sort slower on arrays than on lists?

### Merge sort


```python
def mergeList(A, B):
    (m, n) = (len(A), len(B))
    (C, i, j, k) = ([], 0, 0, 0)
    while k < m + n:
        if i == m:
            C.append(B[j])
            (j, k) = (j + 1, k + 1)
        elif j == n:
            C.append(A[i])
            (i, k) = (i + 1, k + 1)
        elif A[i] < B[j]:
            C.append(A[i])
            (i, k) = (i + 1, k + 1)
        else:
            C.append(B[j])
            (j, k) = (j + 1, k + 1)
    return C
```


```python
def mergesortList(L):
    n = len(L)

    if n <= 1:
        return L

    Left = mergesortList(L[: n // 2])
    Right = mergesortList(L[n // 2 :])

    Lsorted = mergeList(Left, Right)

    return Lsorted
```


```python
def mergeArray(A, B):
    (m, n) = (np.prod(A.shape), np.prod(B.shape))
    (C, i, j, k) = (np.zeros(m + n, dtype=int), 0, 0, 0)
    while k < m + n:
        if i == m:
            C[k] = B[j]
            (j, k) = (j + 1, k + 1)
        elif j == n:
            C[k] = A[i]
            (i, k) = (i + 1, k + 1)
        elif A[i] < B[j]:
            C[k] = A[i]
            (i, k) = (i + 1, k + 1)
        else:
            C[k] = B[j]
            (j, k) = (j + 1, k + 1)
    return C
```


```python
def mergesortArray(A, l, r):
    if r - l <= 1:
        B = np.array(A[l:r])
        return B

    mid = (l + r) // 2

    L = mergesortArray(A, l, mid)
    R = mergesortArray(A, mid, r)

    B = mergeArray(L, R)

    return B
```

### Perfomance on large inputs, $10^7$, random and sorted


```python
import random

random.seed(2021)
inputlists = {}
inputlists["random"] = [random.randrange(100000000) for i in range(1000000)]
inputlists["ascending"] = [i for i in range(1000000)]
inputlists["descending"] = [i for i in range(999999, -1, -1)]
t = Timer()
for k in inputlists.keys():
    tmplist = inputlists[k][:]
    t.start()
    mergesortList(tmplist)
    t.stop()
    print(k, t)
```

    random 9.461006794999776
    ascending 7.209758885000156
    descending 7.549550362000446



```python
import numpy as np
import random

random.seed(2021)
inputarrays = {}
inputarrays["random"] = np.arange(1000000)
for i in range(1000000):
    inputarrays["random"][i] = random.randrange(100000000)
inputarrays["ascending"] = np.arange(1000000)
inputarrays["descending"] = np.arange(999999, -1, -1)
t = Timer()
for k in inputarrays.keys():
    tmparray = inputarrays[k][:]
    t.start()
    mergesortArray(tmparray, 0, 1000000)
    t.stop()
    print(k, t)
```

    random 50.28121324999938
    ascending 45.242545600000085
    descending 47.68783998900017



```python
def quicksortList(L, l, r):  # Sort L[l:r]
    if r - l <= 1:
        return L
    (pivot, lower, upper) = (L[l], l + 1, l + 1)
    for i in range(l + 1, r):
        if L[i] > pivot:  # Extend upper segment
            upper = upper + 1
        else:  # Exchange L[i] with start of upper segment
            (L[i], L[lower]) = (L[lower], L[i])
            # Shift both segments
            (lower, upper) = (lower + 1, upper + 1)
    # Move pivot between lower and upper
    (L[l], L[lower - 1]) = (L[lower - 1], L[l])
    lower = lower - 1
    # Recursive calls
    quicksortList(L, l, lower)
    quicksortList(L, lower + 1, upper)
    return L
```


```python
def quicksortArray(A, l, r):  # Sort A[l:r]
    if r - l <= 1:
        return A
    (pivot, lower, upper) = (A[l], l + 1, l + 1)
    for i in range(l + 1, r):
        if A[i] > pivot:  # Extend upper segment
            upper = upper + 1
        else:  # Exchange L[i] with start of upper segment
            (A[i], A[lower]) = (A[lower], A[i])
            # Shift both segments
            (lower, upper) = (lower + 1, upper + 1)
    # Move pivot between lower and upper
    (A[l], A[lower - 1]) = (A[lower - 1], A[l])
    lower = lower - 1
    # Recursive calls
    quicksortArray(A, l, lower)
    quicksortArray(A, lower + 1, upper)
    return A
```

### Quicksort performance
- Random input of size $10^7$
    - Compare with merge sort on $10^7$ random input
- Sorted inputs of size $2 \times 10^4$


```python
import random

random.seed(2021)
inputlists = {}
inputlists["random"] = [random.randrange(100000000) for i in range(1000000)]
inputlists["ascending"] = [i for i in range(20000)]
inputlists["descending"] = [i for i in range(19999, -1, -1)]
t = Timer()
for k in inputlists.keys():
    tmplist = inputlists[k][:]
    t.start()
    quicksortList(tmplist, 0, len(tmplist))
    t.stop()
    print(k, t)
```

    random 6.846926215000053
    ascending 23.762334613999997
    descending 43.71380329099998



```python
import numpy as np
import random

random.seed(2021)
inputarrays = {}
inputarrays["random"] = np.arange(1000000)
for i in range(1000000):
    inputarrays["random"][i] = random.randrange(100000000)
inputarrays["ascending"] = np.arange(20000)
inputarrays["descending"] = np.arange(19999, -1, -1)
t = Timer()
for k in inputarrays.keys():
    tmparray = inputarrays[k][:]
    t.start()
    quicksortArray(tmparray, 0, np.prod(tmparray.shape))
    t.stop()
    print(k, t)
```

    random 12.35117238500004
    ascending 46.47526735700001
    descending 96.12570456000003

