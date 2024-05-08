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
        if self.elapsed == None and self._start_time== None:
            raise TimerError("the counter not running")
        else:
            self.stop()
            return self.elapsed_time
    def __str__(self) -> str:
        return (str(self.elapsed_time))


T =TimerError()
T.start()
end_time = T.elapsed()
lg.info(f"time taken:{end_time}")
```

    [32m2024-05-08 17:13:40.450[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m38[0m - [1mtime taken:1.1658004950731993e-05[0m



```python
L = [ random.randint(1,1000000000) for i in range(10000)]
```


```python
v = random.randint(1,1000000)
```

# Naive Approach 


```python
def naive_search(V,L):
    for x in L:
        if V==x:
            return True 
    else:
        return False 
    
    
```

complexity = O(n)


```python
T =TimerError()
T.start()
print(f"length of L :{len(L)}")
print(naive_search(v,L))
end_time = T.elapsed()
lg.info(f"time taken:{end_time}")
```

    [32m2024-05-08 17:13:40.480[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime taken:0.00020517699886113405[0m


    length of L :10000
    False


# binary search 

# sorting function 


```python
def sort_list(L: list):
    if len(L) ==0:
        return []
    midpoint = len(L)//2
    mid_value = L[midpoint]
    lower_list = [low for low in L if low < mid_value]
    mid_list = [mid for mid in L if mid == mid_value]
    upper_list = [ upper for  upper in L if  upper > mid_value]
    return sort_list(lower_list)+mid_list+sort_list(upper_list)
```


```python
midpoint = len(L)//2
mid_value = L[midpoint]
```


```python
T =TimerError()
T.start()
print(f"length of L :{len(L)}")
sort_list(L)
end_time = T.elapsed()
lg.info(f"time taken:{end_time}")
```

    [32m2024-05-08 17:13:40.512[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime taken:0.012002756993751973[0m


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
T =TimerError()
T.start()
print(f"length of L :{len(L)}")
L = sort_list(L)
end_time = T.elapsed()
lg.info(f"time taken:{end_time}")
```

    [32m2024-05-08 17:13:40.538[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime taken:0.009969204023946077[0m


    length of L :10000



```python
def binarysearch(v: int ,L : list)-> bool:
    
    if not L:
        return False 
    midpoint = len(L) // 2
    
    if v == L[midpoint]:
        return True 
    if v < L[midpoint]:
        return binarysearch(v, L[:midpoint])
    else:
        return binarysearch(v, L[midpoint+1:])
```


```python
T =TimerError()
T.start()
print(f"length of L :{len(L)}")
print(binarysearch(v,L))
end_time = T.elapsed()
lg.info(f"time taken:{end_time}")
```

    [32m2024-05-08 17:13:40.554[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime taken:0.0001781220198608935[0m


    length of L :10000
    False


Complexity = O(logn)
