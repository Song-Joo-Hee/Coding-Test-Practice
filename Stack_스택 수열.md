### 문제
* 백준 1874번<br>

스택의 수를 push할 때는 반드시 오름차순으로만 push
스택을 쌓다가 필요한 타이밍에 pop하게 되는데 pop을 한 수를 나열했을때, n줄에 걸쳐 입력한 수열과 같아야 한다.

```python
import sys

input = sys.stdin.readline

n = int(input())
stack = []
current_num = 1 # 오름차순이니까 1로 초기화
answer = []
flag = 0

for i in range(n):
    num = int(input())
    while current_num <= num : # 내가 입력한 수가 될때까지 +1 해주면서 push해준다.
        stack.append(current_num)
        answer.append('+')
        current_num += 1

    if stack[-1] == num : # 스택의 마지막 값이 입력한 숫자와 같다면 pop하여 수열을 만들어준다.
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)
```
