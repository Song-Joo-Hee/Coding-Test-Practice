### 문제 요약.
- 백준 1926번 문제.

**도화지에 그림이 그려져 있을 때, 그림의 개수와 가장 넓이가 넓은 것을 출력하여라.**
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 

### 입력.
* 첫째줄 : 도와지의 세로 크기 n(1<=n<=500)와 가로크기 m(1<=m<=500)
* 두번째 줄 ~ n+1 줄 : 그림의 정보 (단 그림의 정보는 0과 1이 공백을 두고 주어진다.)

### 출력.
* 첫째줄 : 그림의 개수
* 두번째 줄 : 가장 넓은 그림의 넓이 (단, 그림이 하나도 없는 경우는 가장 넓은 그림의 넓이는 0이다.)

### 아이디어.
1. 이중 for문을 돌면서 그래프가 값이 1이면서 방문하지 않는 것에 대해 bfs 수행
2. bfs 돌면서 그림 개수 +1, 최대값을 갱신

### 시간복잡도.
1. O(V+E)
2. V = M*N
3. E = V * 4(넉넉잡아서)
4. 그러므로, 5 * M * N (M과 N은 최대 500이므로, 100만) 1초에 2억개의 연산을 하므로, 가능!

### 자료구조.
1. 그래프 전체 지도 : int[][]
2. 방문 : bool[][]
3. queue(bfs)


```python
from collections import deque

import sys
input = sys.stdin.readline # 입력을 빠르게 받기 위해

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)] # 세로길이만큼 그래프 지도를 채워넣기 -> 2차원 배열 생성
chk = [[False] * m for _ in range(n)] # n*m 만큼 방문 배열(2차원) 생성 -> false로 초기화

dy = [0,1,0,-1] # y축의 이동 방향 -> x축과 세트로 외워두기
dx = [1,0,-1,0] # 오른쪽으로 한칸, 밑으로 한칸, 왼쪽으로 한칸, 위로 한칸

def bfs(y, x):
    rs = 1 # 넓이를 1로 초기화
    q = deque()
    q.append((y, x)) # 해당 위치를 q에 집어 넣기
    while q:
        ey, ex = q.popleft() # 처음에는 해당 위치를 꺼내게 되고, 그 이후로는 상,하.좌.우에서 1인 경우의 위치를 차례대로 꺼냄.
        for k in range(4): #우, 하, 좌, 상 차례대로
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m: # map의 크기내에 존재해야 함.
                if map[ny][nx] == 1 and chk[ny][nx] == False: # 해당 위치가 1이고, 방문하지 않았을 때
                    rs += 1 # 넓이를 1 증가 시킨다.
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

cnt = 0 # 그림개수
maxv = 0 # 최대넓이값
for j in range(n): # 이중 for문일때, 보통 y부터
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False: # 해당 위치가 1이고, 방문하지 않았을때
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-5-5c9e585c93e7> in <module>
          4 input = sys.stdin.readline # 입력을 빠르게 받기 위해
          5 
    ----> 6 n,m = map(int, input().split())
          7 map = [list(map(int, input().split())) for _ in range(n)] # 세로길이만큼 그래프 지도를 채워넣기 -> 2차원 배열 생성
          8 chk = [[False] * m for _ in range(n)] # n*m 만큼 방문 배열(2차원) 생성 -> false로 초기화
    

    ValueError: not enough values to unpack (expected 2, got 0)

