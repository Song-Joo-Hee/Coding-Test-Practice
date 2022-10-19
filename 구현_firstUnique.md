### 문제
* Codility
* A non-empty array A consisting of N integers is given. The unique number is the number that occurs exactly once in array A.
* Write a function: def solution(A) that, given a non-empty array A of N integers, 
* returns the first unique number in A. The function should return −1 if there are no unique numbers in A.

### 아이디어
* Counter 함수 사용하기.
* 함수 사용하지 않고, dictionary 만들기

```python
# 풀이 1. Counter 함수 사용하기
from collections import Counter

def solution(A):
     answer = -1
     a = Counter(A)
     for i in a:
         if a[i] == 1:
             answer = i
             return answer
     return answer
```

```python
풀이 2. dictionary로 문제풀기

def solution(A):
    counts = {}
    for i in A:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    
    for i in counts:
        if counts[i] == 1:
            return i
    
    return -1
```
