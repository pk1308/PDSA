```python
import os
import numpy as np

os.chdir("..")
os.chdir("..")
from driver_folder.time_driver import TimerError
```

    [1mINFO[0m | [34mtime taken:1.0235002264380455e-05[0m



```python
T = TimerError()
T.start()
end_time = T.elapsed()
print(f"time taken:{end_time}")
```
