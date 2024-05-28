# PDSA with Python, Week 1 - Python Recap: gcd and primality

# **gcd**



## Compute gcd via list of common factors





```python
def gcd(m, n):
    cf = []  # List of common factors
    for i in range(1, min(m, n) + 1):
        if (m % i) == 0 and (n % i) == 0:
            cf.append(i)
    return cf[-1]
```

## Compute gcd using most recent common factor


```python
def gcd(m, n):
    for i in range(1, min(m, n) + 1):
        if (m % i) == 0 and (n % i) == 0:
            mrcf = i
    return mrcf
```

### Let's use the `Timer` class to evaluate naive gcd


```python
import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None
        self._elapsed_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop()")
        self._start_time = time.perf_counter()

    def stop(self):
        """Save the elapsed time and re-initialize timer"""
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start()")
        self._elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

    def elapsed(self):
        """Report elapsed time"""
        if self._elapsed_time is None:
            raise TimerError("Timer has not been run yet. Use .start()")
        return self_elapsed_time

    def __str__(self):
        """print() prints elapsed time"""
        return str(self._elapsed_time)
```

## Experiment with inputs of size $10^6$ to $10^8$


```python
t = Timer()
# 10^6
t.start()
print(6712345, 7654321, gcd(6712345, 7654321))
t.stop()
print(t)
# 10^7
t.start()
print(67812345, 87654321, gcd(67812345, 87654321))
t.stop()
print(t)
# 10^8
t.start()
print(678912345, 987654321, gcd(678912345, 987654321))
t.stop()
print(t)
```

    6712345 7654321 1
    0.608340369000075
    67812345 87654321 9
    6.068647063000071
    678912345 987654321 9
    60.15791690699996


## Recursive gcd using m-n


```python
def gcd(m, n):
    (a, b) = (max(m, n), min(m, n))
    if a % b == 0:
        return b
    else:
        return gcd(b, a - b)
```

## Re-run experiment with inputs of size $10^6$ to $10^8$


```python
t = Timer()
# 10^6
t.start()
print(6712345, 7654321, gcd(6712345, 7654321))
t.stop()
print(t)
# 10^7
t.start()
print(67812345, 87654321, gcd(67812345, 87654321))
t.stop()
print(t)
# 10^8
t.start()
print(678912345, 987654321, gcd(678912345, 987654321))
t.stop()
print(t)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-e0ea3fcfc369> in <module>()
    ----> 1 t = Timer()
          2 # 10^6
          3 t.start()
          4 print(6712345,7654321,gcd(6712345,7654321))
          5 t.stop()


    NameError: name 'Timer' is not defined


## But all is not well.  Python has a small recursion depth (default is 999)


```python
gcd(2, 999)
```




    1




```python
gcd(2, 9999)
```


    ---------------------------------------------------------------------------

    RecursionError                            Traceback (most recent call last)

    <ipython-input-17-438d0c21cfb7> in <module>()
    ----> 1 gcd(2,9999)
    

    <ipython-input-14-f3dc3b415bd2> in gcd(m, n)
          4     return(b)
          5   else:
    ----> 6     return(gcd(b,a-b))
    

    ... last 1 frames repeated, from the frame below ...


    <ipython-input-14-f3dc3b415bd2> in gcd(m, n)
          4     return(b)
          5   else:
    ----> 6     return(gcd(b,a-b))
    

    RecursionError: maximum recursion depth exceeded in comparison


## Can manually set recursion depth to a larger value


```python
import sys

sys.setrecursionlimit(10000)
gcd(2, 9999)
```




    1



## Increasing recursion limit by another factor of 10 causes Colab to crash


```python
import sys

sys.setrecursionlimit(100000)
gcd(2, 99999)
```

## Euclid's algorithm


```python
def gcd(m, n):
    (a, b) = (max(m, n), min(m, n))
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
```

## Re-run experiment with inputs of size $10^6$ to $10^8$


```python
t = Timer()
# 10^6
t.start()
print(6712345, 7654321, gcd(6712345, 7654321))
t.stop()
print(t)
# 10^7
t.start()
print(67812345, 87654321, gcd(67812345, 87654321))
t.stop()
print(t)
# 10^8
t.start()
print(678912345, 987654321, gcd(678912345, 987654321))
t.stop()
print(t)
```

    6712345 7654321 1
    0.0034868870000082097
    67812345 87654321 9
    0.0013390710000749095
    678912345 987654321 9
    0.0009876770000118995


## Can go much further with Euclid's algorithm --- even $10^{16}$ takes only 0.001s



```python
# 10^16
t.start()
print(
    678912345678912345, 987654321987654321, gcd(678912345678912345, 987654321987654321)
)
t.stop()
print(t)
```

    678912345678912345 987654321987654321 9000000009
    0.0016202869999233371


# **Primality**


```python
def factors(n):
    fl = []  # factor list
    for i in range(1, n + 1):
        if (n % i) == 0:
            fl.append(i)
    return fl


def prime(n):
    return factors(n) == [1, n]
```


```python
for i in range(100):
    if prime(i):
        print(i, end=", ")
print()
```

    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 



```python
def primesupto(m):
    pl = []  # prime list
    for i in range(1, m + 1):
        if prime(i):
            pl.append(i)
    return pl
```


```python
print(primesupto(1000))
```

    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]



```python
def firstprimes(m):
    (count, i, pl) = (0, 1, [])
    while count < m:
        if prime(i):
            (count, pl) = (count + 1, pl + [i])
        i = i + 1
    return pl
```


```python
print(firstprimes(100))
```

    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]


## Directly check if n has a non-trivial factor


```python
def prime(n):
    result = True
    for i in range(2, n):
        if (n % i) == 0:
            result = False
    return result
```


```python
for i in range(100):
    if prime(i):
        print(i, end=", ")
print()
```

    0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 


## Note that this incorrectly lists 0 and 1 as prime!

## Compute frequencies of differences between consecutive primes


```python
def primediffs(n):
    lastprime = 2
    pd = {}  # Dictionary for
    # prime diferences
    for i in range(3, n + 1):
        if prime(i):
            d = i - lastprime
            lastprime = i
            if d in pd.keys():
                pd[d] = pd[d] + 1
            else:
                pd[d] = 1
    return pd
```


```python
pd10000 = primediffs(10000)
print(pd10000)
```

    {1: 1, 2: 205, 4: 202, 6: 299, 8: 101, 14: 54, 10: 119, 12: 105, 18: 40, 20: 15, 22: 16, 34: 2, 24: 15, 16: 33, 26: 3, 28: 5, 30: 11, 32: 1, 36: 1}


## $3 - 2 = 1$. Other than this, all differences are even. Why?
