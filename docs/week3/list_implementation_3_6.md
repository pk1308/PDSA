```python
import sys
import random


import os 

os.chdir("..")
os.chdir("..")
print(f" CWD : {os.getcwd()}")
from driver_folder.time_driver import TimerError 
```

     CWD : /home/pk/Desktop/gitmaster/PDSA



```python
T =TimerError()
T.start()
end_time = T.elapsed()
print(f"time taken:{end_time}")
```

    time taken:2.9004004318267107e-05



```python
class Node:
    def __init__(self, v=None):
        self.value = v
        self.next = None

    def isempty(self):
        return self.value is None

    def append(self, value_to_append):
        if self.isempty():
            self.value = value_to_append
        elif self.next is None:
            self.next = Node(value_to_append)
        else:
            self.next.append(value_to_append)

    def insert(self, value_to_insert):
        new_node = Node(value_to_insert)
        new_node.next = self.next
        self.next = new_node
        self.value, new_node.value = new_node.value, self.value

    def delete(self, value_to_delete):
        if self.isempty():
            return

        if self.value == value_to_delete:
            if self.next is not None:
                self.value = self.next.value
                self.next = self.next.next
            else:
                self.value = None
        else:
            if self.next is not None:
                self.next.delete(value_to_delete)

    def __str__(self):
        result = str(self.value)
        if self.next:
            result += ' -> ' + str(self.next)
        return result

        
    
```


```python
l1 = Node()
l1.isempty()
```




    True




```python
l2 = Node(5)
l2.isempty()

```




    False




```python

# Creating a linked list with values 1, 2, 3
head = Node(1)
head.append(2)
head.append(3)
# Output: 1 -> 2 -> 3
print(f"Initial linked list:{head}")  

# Inserting a new node with value 4 after the first node
head.insert(4)
print(f"After inserting 4:{head}")  # Output: 1 -> 4 -> 2 -> 3

# Deleting the node with value 2
head.delete(2)
print(f"After deleting 2:{head}")  # Output: 1 -> 4 -> 3
```

    Initial linked list:1 -> 2 -> 3
    After inserting 4:4 -> 1 -> 2 -> 3
    After deleting 2:4 -> 1 -> 3

