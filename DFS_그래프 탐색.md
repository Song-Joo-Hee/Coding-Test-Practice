### 문제
* 코드트리 intermediate low
* N개의 정점과 M개의 간선으로 이루어진 양방향 그래프가 주어졌을 때, 
* 1번 정점에서 시작하여 주어진 간선을 따라 이동했을 때 도달 할 수 있는 서로 다른 정점의 수를 구하는 프로그램을 작성해보세요.

### 입력
* 첫 번째 줄 : N과 M (1≤N≤1,000), (0≤M≤min(10,000, N(N-1)/2)) 
* 두 번째 줄 : M개의 줄에 걸쳐 (x,y) (1≤x,y≤N)

### 출력
* 1번 정점에서 시작하여 주어진 간선을 따라 이동했을 때 도달 할 수 있는 서로 다른 정점의 수를 출력

```python
import sys
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

visited = [[False] for _ in range(n+1)]
answer = 0

def dfs(vertex):
    global answer

    for next_v in graph[vertex]:
        if visited[next_v] == False:
            visited[next_v] = True
            answer += 1
            dfs(next_v)

for _ in range(n):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited[1] = True
dfs(1)
```
