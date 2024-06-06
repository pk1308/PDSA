## Tower of Hanoi 

![image.png](towerofhanoi_files/image.png)


```python
def tower_of_hanoi(N , from_bar , to_bar , aux_bar):
    if N ==1:
        print("move disk 1 from bar ", from_bar , " to_bar", to_bar)
        return 
    tower_of_hanoi(N-1 , from_bar, aux_bar, to_bar)
    print("move disk " ,N , " from bar ", from_bar , " to_bar", to_bar)
    tower_of_hanoi(N-1 , aux_bar, to_bar, from_bar)
```


```python
n = 4 

tower_of_hanoi(N=n , from_bar="A",aux_bar= "B" ,to_bar= "C")
```

    move disk 1 from bar  A  to_bar B
    move disk  2  from bar  A  to_bar C
    move disk 1 from bar  B  to_bar C
    move disk  3  from bar  A  to_bar B
    move disk 1 from bar  C  to_bar A
    move disk  2  from bar  C  to_bar B
    move disk 1 from bar  A  to_bar B
    move disk  4  from bar  A  to_bar C
    move disk 1 from bar  B  to_bar C
    move disk  2  from bar  B  to_bar A
    move disk 1 from bar  C  to_bar A
    move disk  3  from bar  B  to_bar C
    move disk 1 from bar  A  to_bar B
    move disk  2  from bar  A  to_bar C
    move disk 1 from bar  B  to_bar C



```python

```


```python

```
