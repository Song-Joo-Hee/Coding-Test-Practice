### 문제
* 백준 2667번

```python
"""
1. 아이디어
- 2중 for, 값이 1이고 방문하지 않았으면 -> dfs
- dfs를 통해 찾은 값을 저장후 정렬해서 출력

2. 시간복잡도
- o(v+e)
- v,e : n^2, 4n^2 -> n^2 -> 625 >> 가능

3. 자료구조
- 그래프 저장 : int[][]
- 방문여부 : bool[][]
- 결과값 : int[]
"""

import sys

input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]
result = []
each = 0
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<n and 0<=nx<n:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny,nx)

for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and chk[j][i] == False:
            # 방문체크표시
            chk[j][i] = True
            # dfs로 크기 구하기
            each = 0
            dfs(j,i)
            # 크기를 결과리스트에 넣기
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)


```
