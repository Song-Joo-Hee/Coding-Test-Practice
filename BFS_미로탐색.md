### 문제요약
* 백준 2178번 문제<br>


**N*M** 크기의 배열로 표현되는 미로가 있는데, 미로에서 **1은 이동할 수 있는 칸**이고 **0은 이동할 수 없는 칸**이다.
(1,1)에서 출발하여 (N,M)의 위치로 이동할 때 **지나야하는 최소 칸 수**를 구하시오.<br>

### 입력
* 첫째 줄 : 두 정수 N, M(2 ≤ N, M ≤ 100)
* 두번째 줄 ~ N+1 개줄 : 미로 정보 (각각의 수들은 **붙어서** 입력으로 주어진다.)<br>

### 출력
* 첫째 줄 : 지나야하는 최소 칸 수<br>

### 아이디어
1. 상,하,좌,우로 살피면서 1일 때, 방문정보를 +1 해주면서 도착지점까지 가기(bfs 수행)
2. 도착지점일때 방문정보 출력 

### 시간 복잡도
1. bfs는 o(v+e)
2. 그러므로, v : n*m 이고, e : v*4(최대로 생각했을때) 이기 때문에
3. n*m + n*m*4 = 5*n*m = 5*100*100 = 50000
4. 1초 안에 풀 수 있다. <br>

### 자료구조
1. 미로 정보 : int[][]
2. 방문 정보 : int[][]
3. queue 이용<br>

```python
from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(n)] # 미로정보 -> split이 아닌 경우 한 줄 입력받고 rstrip() 호출 반드시.
chk = [[0]*m for _ in range(n)] # 방문정보는 0으로 초기화


dy = [0,1,0,-1]
dx = [1,0,-1,0]

q = deque([(0,0)]) # 큐에는 처음 위치가 들어갈 수 있도록 초기화
chk[0][0] = 1 # 시작 위치도 세어야 하기 때문에 1로 초기화

while q:
    ey, ex = q.popleft()

    if ey == n-1 and ex == m-1 : # 도착 위치 일때, 방문 정보 출력하기
        print(chk[ey][ex])

    for k in range(4): # 상,하,좌,우로 살피기
        ny = ey + dy[k]
        nx = ex + dx[k]
        if 0<=nx<m and 0<=ny<n: # 미로 안에 해당하는 위치에서만 수행
            if map[ny][nx] == 1 and chk[ny][nx] == 0: # 미로에서 1이고, 아직 방문하지 않은 위치일 때
                chk[ny][nx] = chk[ey][ex] + 1
                q.append((ny,nx))
         
```
