# Quick Sort Algo


```python
def quicksort(List_to_sort , lower_index , upper_index ):
    if upper_index - lower_index <= 1: # base case 
        return List_to_sort
    
    pivot = List_to_sort[lower_index]
    lower = lower_index+1
    upper = upper_index-1
    
    while lower <= upper:
        if List_to_sort[lower] <= pivot:
            lower+=1
        else:
            List_to_sort[lower] , List_to_sort[upper] = List_to_sort[upper] , List_to_sort[lower]
            upper -=1
    List_to_sort[lower_index], List_to_sort[upper] = List_to_sort[upper], List_to_sort[lower_index]
    quicksort(List_to_sort, lower_index=lower_index, upper_index=upper)
    quicksort(List_to_sort , lower_index=upper+1 , upper_index=upper_index)
    return List_to_sort
    
    
    
    
     

```


```python
import sys
import random


import os

os.chdir("..")
os.chdir("..")
from driver_folder.time_driver import TimerError
```


```python
import random 

L = [random.randint(a=1, b = 100000) for i in range(1000000)]

```


```python
J = L.copy()
Z = L.copy()
```


```python
T = TimerError()
T.start()
J.sort()
end_time_1 = T.elapsed()
print(f"time taken:{end_time_1}")
```

    time taken:0.22359681299985823



```python
T = TimerError()
T.start()
quicksort(L, 0 , len(L))
end_time_1 = T.elapsed()
print(f"time taken:{end_time_1}")
```

    time taken:1.6058930050003255



```python
def quicksort(List_to_sort, lower_index, upper_index):
    if upper_index- lower_index <=1:
        return List_to_sort 
    
    pivot , lower, upper = List_to_sort[lower_index] , lower_index+1 , lower_index+1
    
    for i in range(lower_index+1 , upper_index):
        if List_to_sort[i] < pivot:
            List_to_sort[i] , List_to_sort[lower] = List_to_sort[lower] , List_to_sort[i]
            lower+=1 
            upper+=1
        else:
            upper+=1

        List_to_sort[lower-1] , List_to_sort[lower_index] = List_to_sort[lower_index], List_to_sort[lower-1]
        
        quicksort(L, lower_index=lower_index, upper_index=lower-1)
        quicksort(L, lower_index= lower , upper_index=upper)
        return List_to_sort
        


```


```python
T = TimerError()
T.start()
quicksort(Z, 0 , len(L))
end_time_1 = T.elapsed()
print(f"time taken:{end_time_1}")
```

    time taken:2.754399974946864e-05



```python

```
