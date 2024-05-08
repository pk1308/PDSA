```python

import sys
from loguru import logger as lg 
import random
import time



```


```python
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
```


```python
L = [ random.randint(1,1000000000) for i in range(1000000)]
```


```python

```


```python
def MaxELement(L):
    time = TimerError()
    time.start()
    maxval = L[0]
    for i in range(len(L)):
        if L[i] > maxval:
            maxval = L[i]
    end_time = time.elapsed()
    lg.info(f"time take \n {end_time}")
    return maxval
```


```python
MaxELement(L)
```

    [32m2024-05-08 15:07:43.327[0m | [1mINFO    [0m | [36m__main__[0m:[36mMaxELement[0m:[36m9[0m - [1mtime take 
     0.01241532398853451[0m





    999999798



## input size = N 

$$
Overall\ time\ =\ 0( n)
$$

# Example 2 


```python
def noDuplicates(L):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i] == L[j]:
                return(False)
    return(True)
```


```python
T =TimerError()
T.start()
result = noDuplicates(L)
lg.info(result)
end_time = T.elapsed()
lg.info(f"time take \n {end_time}")
```

    [32m2024-05-08 15:07:46.224[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m4[0m - [1mFalse[0m
    [32m2024-05-08 15:07:46.225[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime take 
     2.88110359798884[0m


Time is

$$

\begin{gather*}
Overall\ time\ =( \ n-1) +( n-2) +( n-3) \ ....\ 2+1\ =\ \frac{n( n-1}{2}\\
\\
overall\ time\ =\ O\left( n^{2}\right)
\end{gather*}
$$

# Example 3 

Matrix multiplication 


```python
def matrix_Multiplication(A ,  B):
    (m,n,p) = (len(A),len(B),len(B[0]))
    C = [[ 0 for i in range(p) ]
         for j in range(m) ]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return(C)
```


```python
m , n = 100, 1001
```


```python
A = [[random.randint(1,100) for _ in range(n)]  for j in range(m)]
B = [[random.randint(1,100) for _ in range(m)]  for j in range(n)]
```


```python
len(A[0]) , len(B)
```




    (1001, 1001)




```python
T =TimerError()
T.start()
result = matrix_Multiplication(A,B)
# lg.info(result)
end_time = T.elapsed()
lg.info(f"time take \n {end_time}")
```

    [32m2024-05-08 15:07:46.752[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime take 
     0.4464707520091906[0m



```python
import numpy as np 
```


```python
T =TimerError()
T.start()
result = np.matmul(A,B)
# lg.info(result)
end_time = T.elapsed()
lg.info(f"time take \n {end_time}")
```

    [32m2024-05-08 15:07:46.785[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime take 
     0.019344176980666816[0m


$$
\begin{gather*}
Overall\ time\ \equiv O( MNP) \ \\
Overall\ time\ \equiv O\left( N^{3}\right) \ if\ N\ x\ N\ \ \\
\end{gather*}$$

# example 3 


```python
def numberOfBits(n):
    count = 1
    while n > 1:
        count = count + 1
        n = n // 2
    return(count)
```


```python
T =TimerError()
T.start()
result = numberOfBits(12564665525885888)
# lg.info(result)
end_time = T.elapsed()
lg.info(f"time take \n {end_time}")
```

    [32m2024-05-08 15:07:46.799[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m6[0m - [1mtime take 
     5.3243013098835945e-05[0m


$$Overall\ time\ =\ O( log_{2} n)$$

# example 4 

Tower of hanoi 


```python
# Recursive Python function to solve tower of hanoi 


def TowerOfHanoi(n, from_rod, to_rod, aux_rod): 
	if n == 0: 
		return 	
	TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
	print("Move disk", n, "from rod", from_rod, "to rod", to_rod) 
	TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 


# Driver code 
N = 10
T =TimerError()
T.start()
# A, C, B are the name of rods 
TowerOfHanoi(N, 'A', 'C', 'B') 
end_time = T.elapsed()
lg.info(f"time take \n {end_time}")



```

    [32m2024-05-08 15:07:46.819[0m | [1mINFO    [0m | [36m__main__[0m:[36m<module>[0m:[36m19[0m - [1mtime take 
     0.012417969992384315[0m


    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 5 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 6 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 5 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 7 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 5 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 6 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 5 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 8 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 5 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 6 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 5 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 7 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 5 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 6 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 5 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 9 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 5 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 6 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 5 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 7 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 5 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 6 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 5 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 8 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 5 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 6 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 5 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 7 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 5 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 6 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 5 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 10 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 5 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 6 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 5 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 7 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 5 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 6 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 5 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 8 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 5 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 6 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 5 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 7 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 5 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 6 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 5 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 9 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 5 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 6 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 5 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 7 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 5 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 6 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 5 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 8 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 5 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 6 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 5 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 7 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 5 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 4 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 6 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 4 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 3 from rod C to rod A
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 5 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 3 from rod A to rod B
    Move disk 1 from rod C to rod A
    Move disk 2 from rod C to rod B
    Move disk 1 from rod A to rod B
    Move disk 4 from rod A to rod C
    Move disk 1 from rod B to rod C
    Move disk 2 from rod B to rod A
    Move disk 1 from rod C to rod A
    Move disk 3 from rod B to rod C
    Move disk 1 from rod A to rod B
    Move disk 2 from rod A to rod C
    Move disk 1 from rod B to rod C



```python
def Tower_of_Hanoi(n, from_rod , tp_rod , aux_rod):
    if n: pass
```

$$Overall\ time\ =\ O(n^{2})$$


