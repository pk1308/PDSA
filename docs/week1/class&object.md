```python
class Stack:
    """
    A Last-In-First-Out (LIFO) data structure implemented using a Python list.

    Attributes:
        __a (list): The internal list used to store the stack elements.
    """

    def __init__(self) -> None:
        """
        Initializes an empty stack.
        """
        self.__a = []

    def pop(self):
        """
        Removes and returns the element at the top of the stack (the last element added).

        Returns:
            The value at the top of the stack, or -1 if the stack is empty.
        """
        if self.__a:
            return self.__a.pop()
        else:
            return -1

    def push(self, value):
        """
        Adds a new element to the top of the stack.

        Args:
            value: The element to be pushed onto the stack.
        """
        self.__a.append(value)

    def peek(self):
        """
        Returns the element at the top of the stack without removing it.

        Returns:
            The value at the top of the stack, or -1 if the stack is empty.
        """
        if self.__a:
            return self.__a[-1]
        else:
            return -1

    def __str__(self):
        """
        Returns a string representation of the stack (useful for debugging).

        Returns:
            A string representation of the stack contents.
        """
        return str(self.__a)

    def __dict__(self):
        """
        Returns a dictionary representing the stack's attributes (for debugging).

        Returns:
            A dictionary containing the stack's attributes.
        """
        return self.__dict__

        
        
    
```


```python
my_stack = Stack()

# Push elements onto the stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Get the top element without removing it
top_element = my_stack.peek()
print(f"Top element: {top_element}")  

# Print the stack contents (for demonstration)
print(f"Stack: {my_stack}") 
```

    Top element: 30
    Stack: [10, 20, 30]



```python
value_removed = my_stack.pop()
print(f"Valued removed : {value_removed}")
# Print the stack contents after removing the element 
print(f"Stack: {my_stack}") 
```

    Valued removed : 30
    Stack: [10, 20]



```python

```
