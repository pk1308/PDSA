```python
def quickselect(L, l, r, k):  # k-th largest in L[l:r]
    if (k < 1) or (k > r - l):
        return None

    (pivot, lower, upper) = (L[l], l + 1, l + 1)
    for i in range(l + 1, r):
        if L[i] > pivot:  # Extend upper segment
            upper = upper + 1
        else:  # Exchange L[i] with start of upper segment
            (L[i], L[lower]) = (L[lower], L[i])
            (lower, upper) = (lower + 1, upper + 1)
    (L[l], L[lower - 1]) = (L[lower - 1], L[l])  # Move pivot
    lower = lower - 1

    # Recursive calls
    lowerlen = lower - l
    if k <= lowerlen:
        return quickselect(L, l, lower, k)
    elif k == (lowerlen + 1):
        return L[lower]
    else:
        return quickselect(L, lower + 1, r, k - (lowerlen + 1))
```


```python
from random import *

A = [randrange(1000) for i in range(200)]
print(A)
```

    [185, 791, 479, 898, 102, 424, 191, 736, 104, 20, 582, 783, 367, 300, 239, 840, 866, 401, 853, 640, 875, 897, 213, 136, 207, 244, 365, 677, 771, 371, 400, 184, 804, 429, 647, 637, 67, 172, 638, 32, 288, 951, 804, 466, 327, 208, 735, 163, 647, 217, 976, 880, 356, 510, 88, 311, 917, 958, 787, 127, 861, 379, 120, 885, 679, 454, 336, 262, 772, 327, 606, 957, 438, 364, 382, 288, 739, 757, 843, 889, 235, 737, 998, 364, 416, 338, 627, 783, 245, 878, 777, 820, 685, 381, 157, 74, 946, 284, 621, 636, 132, 863, 700, 587, 738, 346, 43, 395, 973, 991, 602, 350, 13, 708, 214, 959, 396, 666, 774, 144, 780, 790, 786, 5, 356, 72, 972, 956, 725, 9, 390, 298, 162, 945, 641, 419, 251, 995, 251, 510, 210, 1, 562, 892, 579, 806, 268, 344, 290, 667, 776, 216, 976, 525, 551, 104, 91, 384, 638, 203, 521, 672, 937, 162, 630, 103, 328, 764, 866, 406, 981, 243, 612, 741, 562, 858, 229, 307, 717, 787, 861, 569, 859, 960, 790, 949, 496, 318, 532, 135, 57, 177, 100, 422, 446, 609, 401, 602, 457, 571]



```python
for i in range(0, len(A) + 2):
    print(quickselect(A, 0, len(A), i))
```

    None
    1
    5
    9
    13
    20
    32
    43
    57
    67
    72
    74
    88
    91
    100
    102
    103
    104
    104
    120
    127
    132
    135
    136
    144
    157
    162
    162
    163
    172
    177
    184
    185
    191
    203
    207
    208
    210
    213
    214
    216
    217
    229
    235
    239
    243
    244
    245
    251
    251
    262
    268
    284
    288
    288
    290
    298
    300
    307
    311
    318
    327
    327
    328
    336
    338
    344
    346
    350
    356
    356
    364
    364
    365
    367
    371
    379
    381
    382
    384
    390
    395
    396
    400
    401
    401
    406
    416
    419
    422
    424
    429
    438
    446
    454
    457
    466
    479
    496
    510
    510
    521
    525
    532
    551
    562
    562
    569
    571
    579
    582
    587
    602
    602
    606
    609
    612
    621
    627
    630
    636
    637
    638
    638
    640
    641
    647
    647
    666
    667
    672
    677
    679
    685
    700
    708
    717
    725
    735
    736
    737
    738
    739
    741
    757
    764
    771
    772
    774
    776
    777
    780
    783
    783
    786
    787
    787
    790
    790
    791
    804
    804
    806
    820
    840
    843
    853
    858
    859
    861
    861
    863
    866
    866
    875
    878
    880
    885
    889
    892
    897
    898
    917
    937
    945
    946
    949
    951
    956
    957
    958
    959
    960
    972
    973
    976
    976
    981
    991
    995
    998
    None



```python
def MoM(L):  # Median of medians

    if len(L) <= 5:
        L.sort()
        return L[len(L) // 2]

    # Construct list of block medians
    M = []

    for i in range(0, len(L), 5):
        X = L[i : i + 5]
        X.sort()
        M.append(X[len(X) // 2])

    return MoM(M)
```


```python
from random import *

A = [randrange(1000) for i in range(200)]
print(A)
```

    [136, 516, 789, 782, 851, 956, 462, 802, 226, 279, 506, 227, 507, 752, 633, 244, 356, 880, 835, 376, 524, 811, 163, 597, 333, 289, 891, 77, 807, 348, 303, 465, 108, 48, 736, 748, 454, 278, 854, 192, 581, 384, 96, 641, 821, 149, 908, 410, 192, 892, 303, 664, 144, 878, 147, 699, 908, 633, 485, 601, 73, 820, 723, 516, 941, 175, 785, 309, 67, 30, 341, 322, 252, 792, 698, 888, 780, 926, 559, 983, 650, 905, 20, 382, 440, 227, 306, 673, 987, 130, 47, 396, 511, 850, 940, 48, 785, 757, 965, 997, 227, 701, 297, 700, 532, 664, 832, 32, 146, 330, 900, 149, 409, 205, 371, 123, 554, 989, 654, 286, 44, 993, 134, 182, 471, 479, 149, 952, 270, 292, 950, 87, 614, 160, 459, 762, 848, 277, 547, 798, 778, 516, 932, 268, 433, 892, 146, 470, 266, 115, 856, 27, 462, 841, 535, 702, 874, 783, 816, 948, 134, 837, 520, 497, 444, 792, 252, 131, 814, 579, 244, 51, 801, 169, 825, 510, 19, 602, 407, 917, 737, 333, 918, 758, 190, 573, 844, 816, 986, 880, 990, 672, 218, 752, 227, 262, 941, 946, 678, 93]



```python
B = sorted(A)
(B[(3 * len(B)) // 10], B[len(B) // 2], B[(7 * len(B)) // 10], MoM(A))
```




    (297, 520, 782, 535)




```python
import sys

sys.setrecursionlimit(2**31 - 1)
```


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
        return self._elapsed_time

    def __str__(self):
        """print() prints elapsed time"""
        return str(self._elapsed_time)
```


```python
t = Timer()
t.start()
A = [i for i in range(10000)]
print(quickselect(A, 0, len(A), 10000))
t.stop()
print(t)
```

    9999
    7.300186226999813



```python
def fastselect(L, l, r, k):  # k-th largest in L[l:r]
    if (k < 1) or (k > r - l):
        return None

    # Find MoM pivot and move to L[l]
    pivot = MoM(L[l:r])
    pivotpos = min([i for i in range(l, r) if L[i] == pivot])
    (L[l], L[pivotpos]) = (L[pivotpos], L[l])

    (pivot, lower, upper) = (L[l], l + 1, l + 1)
    for i in range(l + 1, r):
        if L[i] > pivot:  # Extend upper segment
            upper = upper + 1
        else:  # Exchange L[i] with start of upper segment
            (L[i], L[lower]) = (L[lower], L[i])
            (lower, upper) = (lower + 1, upper + 1)
    (L[l], L[lower - 1]) = (L[lower - 1], L[l])  # Move pivot
    lower = lower - 1

    # Recursive calls
    lowerlen = lower - l
    if k <= lowerlen:
        return fastselect(L, l, lower, k)
    elif k == (lowerlen + 1):
        return L[lower]
    else:
        return fastselect(L, lower + 1, r, k - (lowerlen + 1))
```


```python
t = Timer()
t.start()
A = [i for i in range(10000)]
print(fastselect(A, 0, len(A), 10000))
t.stop()
print(t)
```

    9999
    0.012660245999541075

