# PDSA with Python, Week 1 - Introducing Jupyter Notebook
## Computing primes from 1 to 100

## Aim of this notebook
* Illustrate how Jupyter/Colab notebooks work
* Interspersing documentation, explanations with the code
* Output is preserved, reloaded when the notebook is opened the next time





## Let's begin

First: a function compute list of factors of a number


```python
def factors(n):
    factorlist = []
    for i in range(1, n + 1):
        if n % i == 0:
            factorlist.append(i)
    return factorlist
```

Next: two different definitions for checking if a number is a prime
1. Note that different definitions can coexist in the notebook
1. When we *run* a cell, that definition becomes the current one
1. The first definition is *intentionally* wrong (the condition in the `return()` should be `==` rather than `!=`)


```python
def prime(n):
    return factors(n) != [1, n]
```


```python
def prime(n):
    return len(factors(n)) == 2
```

Finally, some code that uses the functions defined above to list primes from 1 to 100
* Try it with each of the definitions of `prime()` above
    * Using the second version (the **correct** characterization) you should get the primes from 2 to 97
    * Using the first version (the intentionally **incorrect** version) you should get the composite numbers from 1 to 100


```python
primelist = []
for i in range(1, 101):
    if prime(i):
        primelist.append(i)

print(primelist)
```

    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


## Graphical output
This is to show more interesting forms of output are preserved by the notebook
* Plot $1 + \cos(x)$ for $x \in [0,4\pi)$
    * More precisely, $1 + \cos(2\pi t)$ for $t \in [0,2)$, in discrete increments of $0.01$
* Change $\cos()$ to $\sin()$ and see how the output changes
* **Note**: Markdown supports $\LaTeX$ for math!


```python
import matplotlib.pyplot as plt
import numpy as np

# Create an array t = [0, 0.01, 0.02, ..., 1.99]
t = np.arange(0.0, 2.0, 0.01)

# print(t) will show you the array t

# Compute an array s containing f(t) for each value of t
s = 1 + np.cos(2 * np.pi * t)

# print(s) will show you the array s

# Create the plot of t vs s and display it
fig, ax = plt.subplots()
ax.plot(t, s)

plt.show()
```


    
![png](Lecture%201.2%20-%20Implementation%20of%20Python%20codes%20%28Part%201%29_files/Lecture%201.2%20-%20Implementation%20of%20Python%20codes%20%28Part%201%29_11_0.png)
    

