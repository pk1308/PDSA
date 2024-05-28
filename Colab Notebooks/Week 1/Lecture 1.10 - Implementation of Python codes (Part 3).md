# PDSA with Python, Week 1 - Timing Code

### Define a `Timer` class


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

### Experimentally check Python execution time
* Run a simple loop $10^4, 10^5, \ldots, 10^8$ times
* Time taken ranges from approximately $0.001s$ to approximately $10s$


```python
t = Timer()
for j in range(4, 9):
    t.start()  # Start the timer

    # Run a trivial loop with 10^j iterations
    n = 0
    for i in range(10**j):
        n = n + i

    t.stop()  # Stop the timer
    print(j, t)  # Report time taken for this value of j
```

    4 0.0016220360000005485
    5 0.013152008000005821
    6 0.12692025299999443
    7 1.3113010569999943
    8 12.951606929000008


### If we change the basic operation inside the loop to a constant assignment, the time is slightly less


```python
t = Timer()
for j in range(4, 9):
    t.start()  # Start the timer

    # Run a trivial loop with 10^j iterations
    n = 0
    for i in range(10**j):
        n = 0

    t.stop()  # Stop the timer
    print(j, t)  # Report time taken for this value of j
```

    4 0.0015917349999767794
    5 0.0088671290000093
    6 0.07052080700000829
    7 0.7320572719999916
    8 7.1662828649999994

