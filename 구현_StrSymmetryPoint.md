### 문제
* Codility
* Write a function: def solution(S) that, given a string S, returns the index (counting from 0) of a character 
* such that the part of the string to the left of that character is a reversal of the part of the string to its right. 
* The function should return −1 if no such index exists.

### 아이디어
* 중간을 기준으로 대칭이 되기 위해서는 길이가 홀수여야 한다.
* 길이가 홀수일 때, 중간까지 for문을 돌면서 문자를 비교해본다. 

```python
def solution(S):
    if len(S) % 2 == 1:
        cnt = 0
        mid = len(S) // 2
        for i in range(mid):
            compare = len(S) - (i+1)
            if S[i] == S[compare]:
                cnt += 1
        if cnt == mid :
            return mid
        else:
            return -1
    else:
        return -1
  
```
