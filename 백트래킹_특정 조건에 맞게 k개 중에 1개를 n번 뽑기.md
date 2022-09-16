### 문제.
* 코드트리 intermediate low
* 1이상 K이하의 숫자를 하나 고르는 행위를 N번 반복하여 나올 수 있는 모든 서로 다른 순서쌍을 구해주는 프로그램을 작성해보세요. 
* 단, 연속하여 같은 숫자가 3번 이상 나오는 경우는 제외합니다.

### 입력
* 첫째 줄 : K와 N

### 출력
* 한 줄에 하나씩 조건을 만족하는 순서쌍 (사전 순으로)


```python
k, n = map(int, input().split())
answer = []

def choose(curr_num):
    # 종료 조건
    if curr_num == n+1 :
        print(*answer)
        return 
    # 재귀 함수
    for i in range(1, k+1):
        if curr_num < 3 or not( i == answer[-1] and i == answer[-2]): # 현재 자릿수가 세번째보다 작거나, 그 전 값과 그 전전 값이 같지 않을때
            answer.append(i)
            choose(curr_num+1) # 다음 자리수에 숫자를 넣어준다. 
            answer.pop() # 다음 자리수까지 숫자를 다 넣어주고 n보다 커졌을때 다시 백트래킹한다. 

choose(1)

```
