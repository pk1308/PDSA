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

    time taken:3.456299987192324e-05



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

    time taken:0.7082312540001112



```python
T = TimerError()
T.start()
l = []
for i in range(10**5):
    l.insert(0, i)
end_time = T.elapsed()
print(f"time taken:{end_time}")
```

    time taken:1.2863995140000952



```python
T = TimerError()
T.start()
l = []
for i in range((10**5) * 2):
    l.insert(0, i)
end_time = T.elapsed()
print(f"time taken:{end_time}")
```

    time taken:4.889978135000092



```python
T = TimerError()
T.start()
l = []
for i in range((10**5) * 3):
    l.insert(0, i)
end_time = T.elapsed()
print(f"time taken:{end_time}")
```

    time taken:15.133477557999868



```python

```
