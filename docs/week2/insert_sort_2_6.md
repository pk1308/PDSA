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

    [32m2024-05-08 22:21:09.423[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m37[0m - [1mtime taken:1.105800038203597e-05[0m



```python
L = [ random.randint(1,100) for i in range(1000)]
V= random.randint(1,100)
```

# insertion sort 


```python
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
            j -= 1  # Decrement j to movalue_to_inserte towards the beginning of the list
            
    return L

```


```python
T =TimerError()
T.start()
insertion_sort(L)
end_time = T.elapsed()
lg.info(f"time taken:{end_time}")
```

    [32m2024-05-08 22:47:10.805[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m5[0m - [1mtime taken:0.014249863976147026[0m


$$
\begin{gather*}
outer\ loop\ =\ n\ \\
inner\ loop\ =\ \frac{n( n-1)}{2}\\
\\
complexity\ =\ O\left( n^{2}\right)
\end{gather*}$$


```python
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

```


```python
T =TimerError()
T.start()
ISort(L)
end_time = T.elapsed()
lg.info(f"time taken:{end_time}")
```

    [32m2024-05-08 22:49:07.900[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m5[0m - [1mtime taken:0.003761364030651748[0m


$$
\begin{gather*}

complexity\ =\ O\left( n^{2}\right)
\end{gather*}$$
