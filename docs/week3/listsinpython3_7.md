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

    time taken:1.2912001693621278e-05



```python
zerolist = [0, 0, 0]

zeromatrix = [zerolist, zerolist, zerolist]

zeromatrix[1][1] = 1
print(zeromatrix)
```

    [[0, 1, 0], [0, 1, 0], [0, 1, 0]]



```python
zerolist = [0, 0, 0]

zeromatrix = [zerolist, zerolist.copy(), zerolist]

zeromatrix[1][1] = 1

zeromatrix[0][1] = 2

print(zeromatrix)
```

    [[0, 2, 0], [0, 1, 0], [0, 2, 0]]



```python
import numpy as np

zeromatrix = np.zeros((3, 3))

zeromatrix
```




    array([[0., 0., 0.],
           [0., 0., 0.],
           [0., 0., 0.]])




```python
np.arange(5)
```




    array([0, 1, 2, 3, 4])




```python

```
