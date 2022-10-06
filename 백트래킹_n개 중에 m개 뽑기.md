### 문제
* 코드트리 intermediate low
* 조합 문제
* n개 중에 m개의 숫자를 골라 조합을 만든다.


### 입력
* n,m (1≤m≤n≤10)

### 출력
* 조합의 개수 만큼의 줄에 걸쳐 한 줄에 하나씩 조합의 상태를 공백을 사이에 두고 출력

```python
n, m = map(int,  input().split())
answer = []

def combination(cnt, last_num):
    if cnt == m :
        print(*answer)
        
    #그 직전숫자보다 큰 숫자 넣어주기
    for i in range(last_num+1, n+1):
        answer.append(i)
        combination(cnt+1, i)
        answer.pop()

combination(0,0)
```
