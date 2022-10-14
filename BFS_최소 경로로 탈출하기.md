### 문제
* 코드트리 intermediate low
* n * m 크기의 이차원 영역의 좌측 상단에서 출발하여 우측 하단까지 뱀에게 물리지 않고 탈출하려고 합니다. 
* 이동을 할 때에는 반드시 상하좌우에 인접한 칸으로만 이동할 수 있으며, 뱀이 있는 칸으로는 이동을 할 수 없습니다. 
* 탈출 가능한 경로의 최단 거리를 출력하는 코드를 작성해보세요.

### 입력
* 첫 번째 줄 : n,m (2 ≤ n, m ≤ 100)
* 두 번째 줄 : 각 행에 뱀이 없는 경우 1, 뱀이 있는 경우 0이 입력

### 출력
* 좌측 상단에서 출발하여 우측 하단까지 이동 가능한 경로 중 최단 거리를 출력
* 불가능한 경우 -1을 출력

```python
import sys
from collections import deque

n, m = map(int, input().split())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

# dist[i][j] : 시작점으로부터 (i,j) 지점에 도달하기 위한 최단거리 기록
dist = [
    [0 for _ in range(m)]
    for _ in range(n)
]

q = deque()

visited = [[False for _ in range(m)] for _ in range(n)]
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def push(nx,ny,nd):
    q.append((nx,ny))
    visited[nx][ny] = True
    dist[nx][ny] = nd

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def can_go(x,y):
    return in_range(x,y) and a[x][y] and not visited[x][y]

def bfs(): 
    while q :
        x, y= q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny, dist[x][y]+1)
  
push(0,0,0)
bfs()

if visited[n-1][m-1]:
    print(dist[n-1][m-1])
else:
    print(-1)
```
