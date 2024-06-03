```python
1753 %10
```




    3




```python
1753//10
```




    175




```python
1%2
```




    1




```python
int((10.5))
```




    10




```python
def fun(s):
    p = 0 
    s = s.lower()
    
    for i in range(len(s)):
        if s[i] not in s[:i]:
            p+=1
    return p
```


```python
fun("prince")
```




    6




```python
fun("malayalam")
```




    4




```python
def f(n):
    s = 0 
    for i in range(2,n):
        if n %i ==0 and i % 2 == 1:
            s+=1 
            print(i)
    return s
```


```python
f(60)
```

    3
    5
    15





    3




```python
f(59)
```




    0




```python

1 , 3 , 5 , 15
```


```python
x =1 

while True :
    
    if x%5 = = 0:
        break 
    print(x, end= " ")
    x +=1
```


      Cell In[8], line 5
        if x%5 = = 0:
               ^
    SyntaxError: invalid syntax




```python
print("hello, ", "good Mornig")
```

    hello,  good Mornig



```python

L = [8]


```


```python
print(L.pop(0))
print(L.pop(-1))
print(L)
```

    8



    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Cell In[28], line 2
          1 print(L.pop(0))
    ----> 2 print(L.pop(-1))
          3 print(L)


    IndexError: pop from empty list



```python
a= 24
b = 130 


```


```python
130 %24
```




    10




```python
24%10
```




    4




```python
130/4
```




    32.5




```python
def gcd(m, n ):
    
    a , b = max(m,n) , min(m,n)
    print(1)
    if a%b ==0:
        return b 
    else:
        return gcd(b, a%b)
```


```python
gcd(24,130)
```

    1
    1
    1
    1





    2




```python

```
