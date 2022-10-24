### 문제
* 시뮬레이션도 포함
* 백준 11559번
* https://www.acmicpc.net/problem/11559

### 아이디어
* bfs로 탐색한 다음, 다시 그래프를 정렬해준다.
* 이 문제는 bfs랑 시뮬레이션이 합쳐진 문제기 때문에, bfs를 한 턴의 함수랑 똑같이 생각하면 된다.
* 그러므로, visited도 한 턴마다 계속 초기화 해줘야 한다. (정렬을 하면 각 위치의 값이 매번 달라지기 때문에)

```python
# 입력 받기
# 한 턴 함수
## 상하좌우 돌면서 같으면 체크해주기
## 체크한게 4개 이상이면 +1 해주기
# 터지고 난 후 다시 정렬해주기

'''
bfs
0. 시작점을 큐에 넣는다. visited 체크
1-2. 큐가 비게 될 때까지 반복
1. 큐에서 정점 하나를 꺼낸다.
2. 그 정점에 인접한 애들을 다시 넣는다. + visited 체크
'''

from collections import deque

graph = [list(input()) for _ in range(12)]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]
result = 0


def in_range(x,y):
    return 0<=x<=11 and 0<=y<=5

# def can_go(x,y,value):
#     return in_range(x,y) and not visited[x][y] and graph[x][y] == value

def bfs(i,j):
    cnt = 1
    flag = 0

    q = deque() # 인접한 애들 중 같은 문자가 있는지를 세어주기 위한 덱
    q.append((i,j))

    change_dot = deque() # 인접한 애들 중 같은 문자인 애들을 폭발시키기 위한 덱
    change_dot.append((i,j))
    visited = [[False] * 6 for _ in range(12)]
    visited[i][j] = True

    while q :
        x, y = q.popleft()
        for dx,dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx,ny) and not visited[nx][ny] and graph[nx][ny] == graph[i][j]:
                q.append((nx,ny))
                change_dot.append((nx,ny))
                visited[nx][ny] = True
                cnt += 1

    if cnt >= 4:
        flag = 1
        for x,y in change_dot:
            graph[x][y] = "."

    return flag


def gravity(): # 중력에 의한거니까 세로로 for문 돌기
    for y in range(6):
        queue = deque()
        for x in range(11, -1, -1):
            if graph[x][y] != '.':
                queue.append(graph[x][y])
        for x in range(11, -1, -1):
            if queue:
                graph[x][y] = queue.popleft()
            else:
                graph[x][y] = '.'


while True:
    chk = 0
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.':
                chk += bfs(i, j)

    if chk == 0:
        print(result)
        break
    else:
        result += 1
    gravity()


```
