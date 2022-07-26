### 문제
* 백준 2693번

```python
import sys

input = sys.stdin.readline

t = int(input())
result = []

for i in range(t):
    info = list(map(int, input().split()))
    info.sort(reverse=True)
    result.append(info[2])

print('\n'.join(map(str,result)))

```
