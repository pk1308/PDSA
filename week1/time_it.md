```python
import time 

start_time = time.perf_counter()
```


```python
end_time = time.perf_counter()
```


```python
start_time- end_time
```




    -0.250828417003504




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
        elif self.elapsed == None and self._start_time != None:
            raise TimerError("the counter not running")
        else:
            self.stop()
            return self.elapsed_time
    def __str__(self) -> str:
        return (str(self.elapsed_time))
```


```python
timer_obj =  TimerError()

for i in range(4,10):
    timer_obj.start()
    for j in range(10**i):
        pass 
    print(f" i: {i} time taken {timer_obj.elapsed()}")
```

     i: 4 time taken 0.00022252700000535697
     i: 5 time taken 0.0022203449916560203
     i: 6 time taken 0.01746416199603118
     i: 7 time taken 0.14385948498966172
     i: 8 time taken 1.4716057649930008
     i: 9 time taken 14.134486352995737



```python
def gcd( m : int , n : int )-> int:
    (a, b) = (max(m,n) , min(m,n))
    if a%b == 0:
        return b 
    else:
        return gcd(b, a-b)
timer_obj.start()
gcd(9000,2)
timer_obj.elapsed()
```




    2.4133012630045414e-05




```python
def gcd( m : int , n : int )-> int:
    (a, b) = (max(m,n) , min(m,n))
    if a%b == 0:
        return b 
    else:
        return gcd(b, a%b)
timer_obj.start()
gcd(9000,2)
timer_obj.elapsed()
```




    2.3304994101636112e-05


