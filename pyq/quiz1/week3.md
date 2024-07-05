What are the shortcomings of merge sort that quick sort aims to address?

the input list is repeatly sorted while using merge sort  but in case of quick sort sorting happens in one pass

meaning the elements which we take as pivot is not looked again in the sorting of the rest of the algo 

Explain the basic principle of the quick sort algorithm.

the  algo chosen a pivot and seprates  elements into two list which is grater and smaller than the pivot 

then the smaller  and greater list is sort in the sepertaltely in the same manner as the earlier 

What is the role of the pivot in quick sort? How is it typically chosen?

pivot is used to sepearter the greater and smaller elements into sep list 

Describe the partitioning process in quick sort.

we choose a pivot and itewrate through the list , if the element is smaller the element is shifted to the left of the pivot . 

after the partition the elemnts on the right will be greater than the pivot 

What is the average time complexity of quick sort? How does it compare to its worst-case scenario?

average = $nlog(n)$

the worst case of = $n^2$ when have a sorted list the worst case can happen when we choose the max value or min value as the pivot 


How can randomization be used to improve quick sort's performance?

this will help us to reduce the bias when the list is sort or any order 


Compare the implementation of lists in Python to a traditional linked list structure.

list in python used array which in turn uses a fixed space in memory even though we dont fully utlise the space 

in linklist we use the constant space as and when required .


What is the time complexity of appending an element to a Python list? Why?

its $O(n)$ because the element in the list has to to shifted n space if we append in the first place 

or if we append at the end and the array is full then the whole value have to be shifted to new bigger array 

so general we take it as 0(n)



Explain the concept of a hash table and how it relates to Python dictionaries.


hash table is concept of storing data using a function eg sha256 to map the space where the data is stored 


Why must dictionary keys in Python be immutable?

python dic uses hash function to map key and value , if the key is mutable , the system will not be able to find the location
