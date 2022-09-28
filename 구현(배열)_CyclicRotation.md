### 문제 
* from codility
* 어떤 배열에서 값을 오른쪽으로 한 칸씩 밀 때, 출력되는 배열

### 아이디어
* 배열의 슬라이싱을 이용한다. 

```python
def solution(A, K):
    n = 0
    while n < K :
        n += 1
        A = A[-1:] + A[:-1] # 맨 마지막 값을 처음으로 땡겨오고, 나머지를 차례대로 붙인다.
    
    return A
```
