### 문제
* 코드트리 intermediate low
* 1이상 K이하의 숫자를 하나 고르는 행위를 N번 반복하여 나올 수 있는 모든 서로 다른 순서쌍을 구해주는 프로그램을 작성해라.

### 입력
* 첫번째 줄:  K와 N (1≤K≤4 , 1≤N≤8)

### 출력
* 한 줄에 하나씩 순서쌍의 상태를 공백을 사이에 두고 출력 (이때 앞에서 부터 봤을 때 사전순으로 앞선 순서쌍부터 출력)

```python
k, n = map(int, input().split())
answer = []
'''
재귀함수
1. 종료조건 : n+1일때 프린트
2. n일때 append하고 n+1로 넘어가기 
3. 그 후, pop해주고 그 다음 숫자 append 해주기
'''
def choose(cnt):
    # 종료 조건
    if cnt == n+1:
        print(*answer)
        return 
    for i in range(1, k+1):
        answer.append(i)
        choose(cnt+1)
        answer.pop()

choose(1)
```
