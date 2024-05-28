# PDSA with Python, Week 1 - Classes and objects

### Basic definition of class `Point` using $(x,y)$ coordinates


```python
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def translate(self, deltax, deltay):
        self.x += deltax
        self.y += deltay

    def odistance(self):
        import math

        d = math.sqrt(self.x * self.x + self.y * self.y)
        return d
```

Create two points


```python
p = Point(3, 4)
q = Point(7, 10)
```

Compute `odistance` for `p` and `q`


```python
p.odistance(), q.odistance()
```




    (5.0, 12.206555615733702)



Translate `p` and check the distance


```python
p.translate(3, 4)
p.odistance()
```




    10.0



* At this stage, `print()` does not produce anything meaningful
* `+` is not defined yet


```python
print(p)
```

    <__main__.Point object at 0x7f3b302c0750>



```python
print(p + q)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-1886228b68be> in <module>()
    ----> 1 print(p+q)
    

    TypeError: unsupported operand type(s) for +: 'Point' and 'Point'


## Now change the definition of `Point` to use $(r,\theta)$ representation


```python
import math


class Point:
    def __init__(self, a=0, b=0):
        self.r = math.sqrt(a * a + b * b)
        if a == 0:
            self.theta = 0
        else:
            self.theta = math.atan(b / a)

    def translate(self, deltax, deltay):
        x = self.r * math.cos(self.theta)
        y = self.r * math.sin(self.theta)
        x += deltax
        y += deltay
        self.r = math.sqrt(x * x + y * y)
        if x == 0:
            self.theta = 0
        else:
            self.theta = math.atan(y / x)

    def odistance(self):
        return self.r
```

### Repeat the examples above
* Observe that nothing changes for the user of the class

Create two points


```python
p = Point(3, 4)
q = Point(7, 10)
```

Compute `odistance` for `p` and `q`


```python
p.odistance(), q.odistance()
```




    (5.0, 12.206555615733702)



Translate `p` and check the distance


```python
p.translate(3, 4)
p.odistance()
```




    10.0




```python
print(p)
```

    <__main__.Point object at 0x7f3b302d98d0>



```python
print(p + q)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-1886228b68be> in <module>()
    ----> 1 print(p+q)
    

    TypeError: unsupported operand type(s) for +: 'Point' and 'Point'


## Return to $(x,y)$ representation, adding `__str__` and `__add__`


```python
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def translate(self, deltax, deltay):
        self.x += deltax
        self.y += deltay

    def odistance(self):
        import math

        d = math.sqrt(self.x * self.x + self.y * self.y)
        return d

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
```

## Again, run the same examples


```python
p = Point(3, 4)
q = Point(7, 10)
```

Compute `odistance` for `p` and `q`


```python
p.odistance(), q.odistance()
```




    (5.0, 12.206555615733702)



Translate `p` and check the distance


```python
p.translate(3, 4)
p.odistance()
```




    10.0



In the following two cells, we see a difference
* Since `__str__` is defined, `print()` gives useful output
* `+` works as expected thanks to the definition for `__add__`




```python
print(p)
```

    (6,8)



```python
print(p + q)
```

    (13,18)

