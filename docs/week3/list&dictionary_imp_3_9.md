```python
import sys
import random
import os

os.chdir("..")
os.chdir("..")
from driver_folder.time_driver import TimerError
```


```python
T = TimerError()
T.start()
end_time = T.elapsed()
print(f"time taken:{end_time}")
```

    time taken:1.2756994692608714e-05



```python
sys.setrecursionlimit(2**31 - 1)
```


```python
T = TimerError()
T.start()
l = []
for i in range(10**7):
    l.append(i)
end_time = T.elapsed()
print(f"time taken:{end_time}")
```

    time taken:0.35971292899921536



```python
T = TimerError()
T.start()
l = []
for i in range(10**5):
    l.insert(0, i)
end_time = T.elapsed()
print(f"time taken:{end_time}")
```

    time taken:0.7846552830014843



```python
T = TimerError()
T.start()
l = []
for i in range((10**5) * 2):
    l.insert(0, i)
end_time = T.elapsed()
print(f"time taken:{end_time}")
```

    time taken:4.565422638988821



```python
T = TimerError()
T.start()
l = []
for i in range((10**5) * 3):
    l.insert(0, i)
end_time = T.elapsed()
print(f"time taken:{end_time}")
```

    time taken:13.601755273004528



```python

```
