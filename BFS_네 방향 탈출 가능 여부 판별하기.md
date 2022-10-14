### 문제
* 코드트리 intermediate low
* n * m 크기의 이차원 영역의 좌측 상단에서 출발하여 우측 하단까지 뱀에게 물리지 않고 탈출하려고 합니다. 
* 이동을 할 때에는 반드시 상하좌우에 인접한 칸으로만 이동할 수 있으며, 뱀이 있는 칸으로는 이동을 할 수 없습니다. 
* 예를 들어 <그림 1>과 같이 뱀이 배치 되어 있는 경우 실선과 같은 경로로 탈출을 할 수 있습니다. 
* 이 때 뱀에게 물리지 않고 탈출 가능한 경로가 있는지 여부를 판별하는 코드를 작성해보세요.

### 입력 
* 첫번째 줄: n,m (2 ≤ n, m ≤ 100)
* 두번째 줄: 각 행에 뱀이 없는 경우 1, 뱀이 있는 경우 0이 입력

### 출력
* 좌측 상단에서 출발하여 우측 하단까지 뱀에게 물리지 않고 탈출 가능한 경로가 있으면 1, 없으면 0을 출력


```python
'''
0. 시작점을 큐에 넣는다. visited 체크
1-2. 큐가 비게 될때까지 반복
1. 큐에서 정점을 하나 꺼낸다.
2. 그 정점에 인접한 애들을 다시 넣는다. + visited 체크
'''
from collections import deque

n,m = map(int, input().split())
snake_info = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dxs = [-1,1,0,0] 
dys = [0,0,-1,1]

q = deque()

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def can_go(x,y):
    return in_range(x,y) and snake_info[x][y] and not visited[x][y]

def bfs():
    # queue에 남은원소가 있을 때 계속 돌림
    while q:
        #1번 과정
        x, y = q.popleft()

        # queue에서 뺀 원소의 사방을 미리보기
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            
            # 갈 수 있는 곳이라면
            if can_go(new_x, new_y):
                #2번 과정
                q.append((new_x,new_y))
                visited[new_x][new_y] = 1

#0번 과정
q.append((0,0))
visited[0][0] = 1
bfs()

print(visited[n-1][m-1])
```
