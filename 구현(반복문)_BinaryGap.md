### 문제
* from codility
* A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
* Write a function that, given a positive integer N, returns the length of its longest binary gap. 
* The function should return 0 if N doesn't contain a binary gap. 

### 출력 
* 바이너리 갭중에 가장 긴 길이를 출력. (만약, 바이너리 갭이 없으면 0 출력)
* 바이너리 갭 : ex. 1000100 이라고 하면, 바이너리 갭은 2개이고, 각각의 길이는 3,2 이다. 

```python
def solution(N):
    binary_N = bin(N)[2:]
    result = []
    cnt = 0
    binary_N = str(binary_N)
    for i in range(1, len(binary_N)): # 2진수의 맨 처음 숫자는 어차피 1이기 때문에 그 다음부터 세준다. 
        if binary_N[i] == '0' :
            cnt += 1
        elif binary_N[i] == '1':
            result.append(cnt)
            cnt = 0
            
    if not result :
        return 0

    return max(result)
```
