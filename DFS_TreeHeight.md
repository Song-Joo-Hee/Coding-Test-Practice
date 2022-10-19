### 문제
* Codility
* 이진트리의 depth(height)를 출력

### 아이디어
* Tree 라이브러리를 처음 사용해보았다.
* (x,l,r) 순으로 담긴다. 
* 왼쪽 트리 깊이와 오른쪽 트리 깊이를 계속해서 비교한다. 

```python
from extratypes import Tree  # library with types used in the task

def dfs(tree, height):
    left_height = 0
    right_height = 0

    if tree.l:
        left_height = dfs(tree.l, height+1)
    if tree.r:
        right_height = dfs(tree.r, height+1)
    
    if tree.l or tree.r:
        return max(left_height, right_height)
    else:
        return height

def solution(T):
    return dfs(T,0)
```
