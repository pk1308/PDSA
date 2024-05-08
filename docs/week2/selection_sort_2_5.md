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
# lg.add(sys.stdout, colorize=True)

T =TimerError()
T.start()
end_time = T.elapsed()
lg.info(f"time taken:{end_time}")
```

    [32m2024-05-08 18:59:53.053[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m38[0m - [1mtime taken:1.0107993148267269e-05[0m



```python
L = [ random.randint(1,1000000000) for i in range(1000000)]
```


```python

def SelectionSort(L):
    n = len(L)
    if n <= 1:
        return(L)
    for i in range(n):
        # Assume L[:i] is sorted
        mpos = i
        # mpos: position of minimum in L[i:]
        for j in range(i+1,n):
            if L[j] < L[mpos]:
                mpos = j
                # L[mpos] : smallest value in L[i:]
                # # Exchange L[mpos] and L[i]
                (L[i],L[mpos]) = (L[mpos],L[i])
                # Now L[:i+1] is sorted
                return(L)
```

$$T(n) =  O(N^{2})$$


```python
T =TimerError()
T.start()
SelectionSort(L)
end_time_1 = T.elapsed()
lg.info(f"time taken:{end_time_1}")
```

    [32m2024-05-08 19:01:03.132[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m5[0m - [1mtime taken:2.2412044927477837e-05[0m



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
T =TimerError()
T.start()
sort_list(L)
end_time_2 = T.elapsed()
lg.info(f"time taken:{end_time_2}")
```

    [32m2024-05-08 19:01:42.396[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m5[0m - [1mtime taken:1.7496046359883621[0m

