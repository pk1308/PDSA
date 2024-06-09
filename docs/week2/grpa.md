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
    if len(L) ==1:
        return L[0]
    
    largest = -1 
    while left < right:
        midpoint = L[(left+right)//2]
        largest = max(largest, L[left], L[right] , midpoint)  # Update largest if temp is greater
        
        if midpoint > L[left] :
            left = (left+right)//2+1
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
L =[2 , 4 , 5 ,7 ,9]
```


```python
findLargest(L)
```




    9




```python
left , right = 0 , len(L)-1
```


```python
largest = -1 
```


```python
left , right
```




    (3, 2)




```python
midpoint = L[(left+right)//2]
largest = max(largest, L[left], L[right] , midpoint)  # Update largest if temp is greater
largest
        
```




    9




```python
if midpoint > L[left] :
            left = (left+right)//2+1
else:
    right = (left+right)//2-1
```


```python
def selectionsort(L : list) -> list :
    number_of_elements = len(L)
    if number_of_elements<= 1:
        return L
    for i in range(number_of_elements):
        index_to_sort = i 
        for j in range(i+1, number_of_elements):
            if L[j] < L[index_to_sort]:
                L[j] , L[index_to_sort] = L[index_to_sort] , L[j]
    return L
```


```python
selectionsort(L)
```




    [2, 4, 5, 7, 9]




```python

```


```python
class MyList:
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def swap(self, indexA, other, indexB):
        if isinstance(other, MyList):
            self.data[indexA], other.data[indexB] = other.data[indexB], self.data[indexA]
        else:
            self.data[indexA], self.data[other] = self.data[other], self.data[indexA]
```


```python
def mergeInPlace(first_list , second_list):
    len_of_first , len_of_second = len(first_list) , len(second_list)
    pointer_first , pointer_second = 0, 0 
    
    while pointer_first < len_of_first and pointer_second < len_of_second:
        if first_list[pointer_first] <= second_list[pointer_second]:
            pointer_first+=1 
        else:
            first_list.swap(pointer_first, second_list, pointer_second)
        # temp pointer to sorted second list 
        k = pointer_second
        while k < len_of_second-1 and second_list[k] > second_list[k+1]:
            second_list.swap(k, second_list, k+1)
            k+=1
        pointer_first+=1
    return first_list , second_list    
```


```python
def mergeInPlace(first_list , second_list):
    len_of_first , len_of_second = len(first_list) , len(second_list)
    for first_index in range(len_of_first):
        for second_index in range(len_of_second):
            if first_list[first_index] > second_list[second_index]:
                first_list.swap(first_index, second_list, second_index)
    for second_index in range(len_of_second):
        for j in range(second_index+1, len_of_second):
            if second_list[second_index] > second_list[j]:
                second_list.swap(second_index, second_list, j)
    return first_list , second_list    
```


```python
A = MyList([2,4 ,6 ,9 ,13 ,15])
B = MyList([1 ,3 ,5 ,10])
mergeInPlace(A, B)
print(A.data)  # Output: [1, 2, 3]
print(B.data)  # Output: [4, 5, 6]

```

    [1, 2, 3, 4, 5, 6]
    [9, 10, 13, 15]



```python

```
