#!/usr/bin/env python
# coding: utf-8

# In[1]:


#### 2차원 방향 벡터

#동, 북, 서, 남

dx = [ 0, -1, 0, 1]
dy = [1, 0, -1, 0]

#현재 위치
x,y = 2,2

for i in range(4):
    #다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)


# In[2]:


######### 문제 1
# 여행가 a는 n*n 크기의 정사각형 공간 위에 서있다. 이 공간은 1*1 크기의 정사각형으로 나누어져 있다. 가장 왼쪽 위 좌표는 (1,1)이며, 
# 가장 오른쪽 아래 좌표는 (n,n)에 해당한다. 여행가 a는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)이다.
# 우리 앞에는 여행가 a가 이동할 계획이 적힌 계획서가 있다.

# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여, L, R, U, D 중 하나의 문자가 반복적으로 적혀있다. 
# L : 왼쪽으로 한 칸 이동
# R : 오른쪽으로 한 칸 이동
# U : 위로 한 칸 이동
# D : 아래로 한 칸 이동

# 이 때, 정사각형을 벗어나는 움직임은 무시된다.


# In[11]:


# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)

##다시 보기 계산이 안맞음.


# In[12]:


####### 문제 3
# 정수 n이 입력되면 00시 00분 00초부터 n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 
# 모든 경우의 수를 구하는 프로그램을 작성하세요.

#이 문제는 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제. 
# 완전 탐색으로, 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지 확인.   


# In[13]:


# 입력 받기
h = int(input())

count = 0
for i in range(h+1): # 시
    for j in range(60): # 분
        for k in range(60): # 초
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)
            


# In[14]:


####### 문제 4
# 8*8 좌표 평면에 나이트가 움직일 수 있는 방법의 수는 ?
# 나이트는 L자 형태로만 움직일 수 있다. (수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동 / 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동)


# In[16]:


#현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 #아스키코드로 바꿔주기 

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2,1), (1,2), (-1,2), (-2,1)]

#8가지 방향에 대하여 각 위치로 이동 가능 확인 
result = 0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)


# In[17]:


######## 문제 5
# 문자와 숫자를 입력 받아, 문자를 오름 차순으로, 숫자는 입력받은 모든 숫자를 합한 값을 차례로 나열하도록 해야한다.


# In[18]:


data = input()
result = []
value = 0

#문자를 하나씩 확인
for x in data :
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자를 따로 더하기
    else:
        value += int(x)
        
#알파벳은 오름차순으로 정렬
result.sort()

#숫자가 하나라도 존재하는 경우, 가장 뒤에 삽입 
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))


# In[ ]:




