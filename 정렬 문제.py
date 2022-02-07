#!/usr/bin/env python
# coding: utf-8

# In[21]:


import time

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

#선택정렬

start_time = time.time()

for i in range(len(array)):
    max_index = i 
    for j in range(i+1, len(array)):
        if array[max_index] < array[j]:
            max_index = j
    array[i], array[max_index] = array[max_index], array[i] 

print(array)
end_time = time.time()
print('선택 정렬 성능 측정:', end_time - start_time)


# In[22]:


import time

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

#삽입정렬

start_time = time.time()

for i in range(1, len(array)):
    for j in range(i, 0, -1): 
         if array[j] > array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
         else: 
            break  

print(array)
end_time = time.time()
print('삽입 정렬 성능 측정:', end_time - start_time)


# In[23]:


import time

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

#퀵정렬

start_time = time.time()

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x > pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x <= pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

end_time = time.time()
print('퀵 정렬 성능 측정:', end_time - start_time)


# In[24]:


import time

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

#기본 라이브러리 정렬

start_time = time.time()

array.sort(reverse=True)

print(array)

end_time = time.time()
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time)

