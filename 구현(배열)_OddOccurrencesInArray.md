### 문제
* from codility
* A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.
* Write a function: that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.
* Write an efficient algorithm for the following assumptions:
* N is an odd integer within the range [1..1,000,000];
* each element of array A is an integer within the range [1..1,000,000,000];
* all but one of the values in A occur an even number of times.

### 출력
* 짝이 맞지 않는 값을 출력

### 아이디어
* Counter 함수를 이용하여 리스트 안에 담긴 값들의 개수를 각 각 세어준다.
* 짝이 맞지 않는 것은 무조건 홀수개 임을 활용하자. 

```python 
from collections import Counter

def solution(A):
   info = Counter(A)
   for i in info:
       if info[i] % 2 == 1:
           return i
```
