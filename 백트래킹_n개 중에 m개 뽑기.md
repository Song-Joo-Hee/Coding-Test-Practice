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
<br>

* 만약에 조합의 개수를 묻는 문제라면? n개의 공 중에 m개를 뽑았다고 생각하자.
* 4개의 공 중에 3개의 공이라고 치면, 0000 ~ 1111 까지 중에서 1이 3개 있는 이진수의 개수를 출력하면 된다.
```python
# n개의 공 중에 m개 뽑기 
n, m = map(int,  input().split())
answer = []

def combination(curr_num, cnt):
    if curr_num == n+1:
        if cnt == m :
            print(*answer)
        return

    answer.append(0)
    combination(curr_num+1, cnt)
    answer.pop()

    answer.append(1)
    combination(curr_num+1, cnt+1)
    answer.pop(1)

combination(1,0)
```
