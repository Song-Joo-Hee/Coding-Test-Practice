### 문제
* from codility
* 주어진 정수 N을 2의 거듭제곱으로 나눌때 가장 큰 수를 출력.

### 출력
* 2의 거듭제곱 수를 출력 

### 아이디어
* log 함수와 거듭제곱 연산 이용
* 처음에는 log 함수와 거듭제곱을 생각 못해서 구현을 다 해주었다.

```python
# 첫번째 풀이

curr_num = 2
cnt = 1
N = 256
 
while True:
     curr_num *= 2
     cnt += 1
     if curr_num >= N:
         break
         
while True:
    if N % curr_num == 0:
        break
    curr_num = curr_num // 2
    cnt -= 1

print(cnt)
```
<br>

```python
# 두번째 풀이
import math

def solution(N):
    cnt = int(math.log2(N))
    curr_num = (2 ** cnt)

    while True:
        if N % curr_num == 0:
            break
        curr_num = curr_num // 2
        cnt -= 1

    return cnt
```
