### 효율적인 화폐 구성

**문제** : 
N가지 종류의 화폐가 있습니다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 합니다. 
이 때, 각 종류의 화폐는 몇 개라도 사용할 수 있습니다. 
M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하세요.

![image](https://user-images.githubusercontent.com/95834067/156953765-bc02f202-93e8-4fc1-aa03-849d52c2ae1b.png)

![image](https://user-images.githubusercontent.com/95834067/156953788-448d894c-ac49-4854-894d-842ff7d9ffce.png)
<br>
👉 **(i-k)원을 만들 수 있는 방법이 존재할 때는, i원을 만드는 최소 개수와 i-k를 만드는 최소 개수에서 화폐 단위 k를 하나 더 해준 즉, 1을 더해준 개수와 비교한다.**  

![image](https://user-images.githubusercontent.com/95834067/156953798-92ae6417-0b22-4030-bba3-d1b6a0cee2ce.png)
![image](https://user-images.githubusercontent.com/95834067/156953808-62d4cbce-fb26-411c-abd3-fe77c2a67fa8.png)
![image](https://user-images.githubusercontent.com/95834067/156953810-5039eb15-c842-40da-bfbf-343e43273ee9.png)
![image](https://user-images.githubusercontent.com/95834067/156953815-2529a5e7-16f5-400d-aa6c-39de45807ba3.png)


```python
# 정수 N, M을 입력
n, m = map(int, input().split())

# N개의 화폐 단위 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# DP 테이블 초기화
d = [10001] * (m+1) # INF를 표현하기 위해, M의 범위를 벗어나는 값 10001 세팅 

# 보텀업(상향식) - 반복문을 이용한 점화식 구현
d[0] = 0 
for i in range(n):
    for j in range(array[i], m+1) : # 해당 화폐 단위부터 마지막까지 범위 정하기
        if d[j-array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]]+1) # 점화식 구현


# 계산된 결과 출력
if d[m] == 10001 : 
    print(-1)
else :
    print(d[m])
```
<br>
출처 : 이것은 취업을 위한 코딩 테스트다. (https://www.youtube.com/watch?v=5Lu34WIx2Us&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=7)
