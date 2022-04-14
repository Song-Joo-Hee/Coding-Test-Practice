### 문제 요약
* 백준 2667번 문제. <br>

정사각형의 모양의 지도가 있는데, 1은 집이 있는 곳을 0은 집이 없는 곳을 의미한다. <br>
철수는 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려고 한다. <br>

### 입력
* 첫째줄 : 지도의 크기 (5<=N<=25)
* N개의 줄 : N개의 자료(0혹은1)가 입력<br>

### 출력
* 첫째줄 : 총 단지수
* 단지 수만큼의 줄 : 각 줄마다 오름차순으로 각 단지내 집의 수<br>

### 아이디어
1. 상,하,좌,우로 살피면서 근접해있는 1을 찾는다.(bfs)
2. 이때, 지도에서 1이거나 방문하지 않은 위치일때, 개수를 +1 하면서 전체 개수를 세준다. 
3. 탐색이 끝났으면 단지 수 +1을 해준다. <br>

### 시간 복잡도
1. bfs -> o(v+e)
2. v : n
3. e : n*4
4. 그러므로, 5n 즉, 최대 125 이므로 1초 안에 수행 가능하다.<br>

### 자료 구조
1. 지도정보 : int[][]
2. 방문정보 : bool[][]
3. queue 사용

```python

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().rstrip())) for _ in range(n)]
chk = [[False]*n for _ in range(n)]
cnt_list = [] # 단지 내 개수 리스트
rst = 0  # 총 단지 개수

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    cnt = 1 # 각 단지 내 개수
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<n:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    cnt += 1
                    q.append((ny,nx))
    return cnt

for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt_list.append(bfs(j,i))
            rst += 1
cnt_list.sort()

print(rst)
for i in range(rst):
    print(cnt_list[i])
```
