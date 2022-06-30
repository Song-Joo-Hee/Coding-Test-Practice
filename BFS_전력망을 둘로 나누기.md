### 문제
* 프로그래머스 위클리 챌린지 lv.2 전력망을 둘로 나누기

### 아이디어
* 둘로 나눴을때, 한쪽만 bfs로 탐색해서 비교해본다.

```python
from collections import deque

def bfs(start, visited, graph):
    queue = deque([start])
    result = 1
    visited[start] = True
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if visited[i] == False:
                result += 1
                queue.append(i)
                visited[i] = True
    return result 

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]

    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for start, not_visit in wires:
        visited = [False]*(n+1)
        visited[not_visit] = True # 전력망을 나누는 기준 
        result = bfs(start, visited, graph)
        if abs(result - (n-result)) < answer :
            answer = abs(result - (n-result))

    return answer
```
