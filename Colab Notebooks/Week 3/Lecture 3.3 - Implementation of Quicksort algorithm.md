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


```python
import sys

sys.setrecursionlimit(2**31 - 1)
```


```python
def quicksort(L, l, r):  # Sort L[l:r]
    if r - l <= 1:
        return
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
    quicksort(L, l, lower)
    quicksort(L, lower + 1, upper)
    return L
```


```python
qlist = [1, 3, 5, 0, 2, 4, 17, 2, -5, 6, 4, 3]
qnew = quicksort(qlist, 0, 12)
print(qnew, qlist)
```

    [-5, 0, 1, 2, 2, 3, 3, 4, 4, 5, 6, 17] [-5, 0, 1, 2, 2, 3, 3, 4, 4, 5, 6, 17]



```python
import random

random.seed(2021)
inputlists = {}
inputlists["random"] = [random.randrange(100000000) for i in range(1000000)]
inputlists["ascending"] = [i for i in range(10000)]
inputlists["descending"] = [i for i in range(9999, -1, -1)]
t = Timer()
for k in inputlists.keys():
    tmplist = inputlists[k][:]
    t.start()
    quicksort(tmplist, 0, len(tmplist))
    t.stop()
    print(k, t)
```

    random 7.063144969999485
    ascending 7.326286120000077
    descending 13.595035135999751



```python
def merge(A, B):
    (m, n) = (len(A), len(B))
    (C, i, j, k) = ([], 0, 0, 0)
    while k < m + n:
        if i == m:
            C.extend(B[j:])
            k = k + (n - j)
        elif j == n:
            C.extend(A[i:])
            k = k + (n - i)
        elif A[i] < B[j]:
            C.append(A[i])
            (i, k) = (i + 1, k + 1)
        else:
            C.append(B[j])
            (j, k) = (j + 1, k + 1)
    return C
```


```python
def mergesort(A):
    n = len(A)

    if n <= 1:
        return A

    L = mergesort(A[: n // 2])
    R = mergesort(A[n // 2 :])

    B = merge(L, R)

    return B
```


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
    mergesort(tmplist)
    t.stop()
    print(k, t)
```

    random 9.585811198000556
    ascending 5.143434890000208
    descending 5.237693461000163

