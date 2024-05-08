```python
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
        if self.elapsed == None and self._start_time== None:
            raise TimerError("the counter not running")
        else:
            self.stop()
            return self.elapsed_time
    def __str__(self) -> str:
        return (str(self.elapsed_time))
# lg.add(sys.stdout, colorize=True)

T =TimerError()
T.start()
end_time = T.elapsed()
lg.info(f"time taken:{end_time}")
```

    [32m2024-05-08 22:56:27.046[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m37[0m - [1mtime taken:1.082499511539936e-05[0m



```python
L = [ random.randint(1,100) for i in range(1000)]
V= random.randint(1,100)
```


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
    L = mergesort(A[:n // 2])
    R = mergesort(A[n // 2:])
    
    # Merge the sorted halves
    B = merge(L, R)
    
    return B



```

$$complexity\ =\ O\left( nlogn\right)$$


```python

T =TimerError()
T.start()
mergesort(L)
end_time = T.elapsed()
lg.info(f"time taken:{end_time}")
```

    [32m2024-05-08 23:07:56.251[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m5[0m - [1mtime taken:0.0008673730189912021[0m



```python

```
