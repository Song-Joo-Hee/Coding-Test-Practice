### 문제
* 코드트리 intermediate low
* n * m 크기의 이차원 영역의 좌측 상단에서 출발하여 우측 하단까지 뱀에게 물리지 않고 탈출하려고 합니다. 
* 이동을 할 때에는 반드시 아래와 오른쪽 2방향 중 인접한 칸으로만 이동할 수 있으며, 뱀이 있는 칸으로는 이동을 할 수 없습니다. 
* 예를 들어 <그림 1>과 같이 뱀이 배치 되어 있는 경우 실선과 같은 경로로 탈출을 할 수 있습니다. 
* 이 때 뱀에게 물리지 않고 탈출 가능한 경로가 있는지 여부를 판별하는 코드를 작성해보세요.

![image](https://user-images.githubusercontent.com/95834067/195531288-55d4fba5-4ceb-4847-877d-ed06eb878dea.png)

### 입력
* 첫 번째 줄 : n,m (2 ≤ n, m ≤ 100)
* 두 번째 줄 : 각 행에 뱀이 없는 경우 1, 뱀이 있는 경우 0이 입력

### 출력
* 뱀에게 물리지 않고 탈출 가능한 경로가 있으면 1, 없으면 0을 출력

```python
n,m = map(int, input().split())
snake = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dxs = [0,1]
dys = [1,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(nx,ny)
    if not in_range(nx,ny):
        return False
    if visited[nx][ny] == 1 or snake[nx][ny] == 1:
        return False
    
    return True

def dfs(x,y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = 1
            dfs(nx, ny)

visited[0][0] = 1
dfs(0,0)

print(visited[n-1][m-1])
```
