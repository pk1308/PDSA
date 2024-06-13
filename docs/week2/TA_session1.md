```python
class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        from bisect import bisect_right
        nums.sort()
        prefix_sums = []
        for num in nums:
            prefix_sums.append(num + (prefix_sums[-1] if prefix_sums else 0))

        answer = []
        for query in queries:
            idx = bisect_right(prefix_sums, query)
            answer.append(idx)

        return answer
    
```


```python
num = [4,5,2,1]
queries = [3,10,21]
```


```python
x = Solution()
x.answerQueries(num, queries)
```




    [2, 3, 4]




```python
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_value = 0
        max_count = 0 
        dict_value = {}
        for value in nums:
            if value in dict_value:
                dict_value[value]+=1
            else:
                dict_value[value]=1
        result = []
        for  key, values in dict_value.items():
            if values == k:
                result.append(key)
        return result 
```


```python
z = Solution()
z.topKFrequent(nums=[1,1,1,2,2,3], k = 2)
```




    [2]




```python
test = {1:2 , 4:5}
```


```python
max(list(test.values()))
```




    5




```python
[7]*7
```




    [7, 7, 7, 7, 7, 7, 7]




```python
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        test = {}
        for value in nums:
            if value in test:
                test[value]+=1
            else:
                test[value]=1
        result = []

        for order in range(3):
            occurrence = test.get(order)

            result.extend([order]*occurrence)
                
        return result
```


```python
x = Solution()

x.sortColors([2,0,2,1,1,0])
```




    [0, 0, 1, 1, 2, 2]




```python
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])  # Sort by starting point
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)  # No overlap, add directly
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])  # Merge overlapping intervals

        return merged

```


```python
x = Solution()

x.merge([[1,4],[0,2],[3,5]])
```




    [[0, 5]]




```python
intervals= [[1,4],[0,2],[3,5]]
intervals.sort()

intervals
```




    [[0, 2], [1, 4], [3, 5]]




```python

```
