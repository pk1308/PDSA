```python
def sort_list(L: list ):
    if len(L) == 0:
        return []
    midpoint = len(L)//2
    mid_value = L[midpoint]
    lower_list = [low for low in L if low < mid_value]
    mid_list = [mid for mid in L if mid == mid_value]
    upper_list = [upper for upper in L if upper > mid_value]
    return sort_list(lower_list) + mid_list + sort_list(upper_list)
def sort_list_descending(L: list) -> list:
    if len(L) == 0:
        return []
    midpoint = len(L)//2
    mid_value = L[midpoint]
    first_list = [first for first in L if int(first[1:]) > int(mid_value[1:])]
    mid_list = [mid for mid in L if int(mid[1:]) == int(mid_value[1:])]
    last_list = [last for last in L if int(last[1:]) < int(mid_value[1:])]
    return sort_list_descending(first_list) + mid_list + sort_list_descending(last_list)

def combinationSort(strList: list) -> list:
    ascending_list , descending_list = [] , []
    master_dict = {}
    
    for value in strList:
        if value[0] in master_dict:
            master_dict[value[0]].append(value)
        else:
            master_dict[value[0]] = [value]
    sorted_keys = sort_list(list(master_dict.keys()))
    for keys in sorted_keys:
        value_to_add = master_dict.get(keys)
        ascending_list.extend(value_to_add)
        if len(value_to_add) > 1:
            descending_list.extend(sort_list_descending(value_to_add))
        else:
            descending_list.extend(value_to_add)
        
    
   
    return ascending_list , descending_list 
    
```


```python
mast_dict = combinationSort(["d34", "g54", "d12", "b87", "g1", "c65", "g40", "g5", "d77"])
```


```python
mast_dict
```




    (['b87', 'c65', 'd34', 'd12', 'd77', 'g54', 'g1', 'g40', 'g5'],
     ['b87', 'c65', 'd77', 'd34', 'd12', 'g54', 'g40', 'g5', 'g1'])




```python
L = ['g54', 'g1', 'g40', 'g5']
```


```python
midpoint = len(L)//2
mid_value = L[midpoint]
first_list = [first for first in L if int(first[1:]) > int(mid_value[1:])]
mid_list = [mid for mid in L if int(mid[1:]) == int(mid_value[1:])]
last_list = [last for last in L if int(last[1:]) < int(mid_value[1:])]
```


```python
first_list
```




    ['g54']




```python
mid_list
```




    ['g40']




```python
last_list
```




    ['g1', 'g5']




```python
def findLargest(L):
    left , right = 0 , len(L)-1
    
    largest = -1 
    while left <= right:
        midpoint = L[(left+right)//2]
        temp = max(L[left], L[right] , midpoint)  # Assign the maximum value to temp
        largest = max(largest, temp, midpoint)  # Update largest if temp is greater
        
        if midpoint > temp :
            left = (left+right)//2-1
        else:
            right = (left+right)//2-1
    return largest
```


```python
L =[7 ,8 ,2 ,4 ,5 ,6]
```


```python
findLargest(L)
```




    8




```python
L =[7 ,8 ,2 ,4 ,5 ,6]
```


```python
left , right = 0 , len(L)-1
```


```python
L[left:right+1]
```




    []




```python
midpoint = L[(left+right)//2]
temp = max(L[left], L[right] , midpoint)  # Assign the maximum value to temp
largest = max(largest, temp, midpoint)
```


```python
largest
```




    8




```python
midpoint, temp
```




    (7, 8)




```python
if midpoint > temp :
    left = (left+right)//2-1
else:
    right = (left+right)//2-1
```


```python

```
