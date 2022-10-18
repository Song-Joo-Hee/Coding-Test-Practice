### 문제
* from codility
* Write a function solution that, given two integers A and B, 
* returns a string containing exactly A letters 'a' and exactly B letters 'b' with no three consecutive letters being the same.
* (in other words, neither "aaa" nor "bbb" may occur in the returned string).

### 아이디어
* 중간에 문자를 끼워넣을 수 있도록 insert 함수 사용하기 

```python
A, B = map(int, input().split())

if A >= B :
    large = 'a'
    small = 'b'

else:
    large = 'b'
    small = 'a'

lst = []
cnt = 0
lst = lst + [large] * max(A,B)

if A + B < 4:
    lst = lst + [small] * min(A,B)
else:
    i = 0
    while i < len(lst) - 1:
        if lst[i] == lst[i+1] and cnt < min(A,B):
            lst.insert(i+2, small)
            cnt += 1
        i += 1

    i = 0
    while i < len(lst)-1 :
        if cnt < min(A,B):
            if lst[i] == large:
                lst.insert(i+1, small)
                cnt += 1
        i += 1


answer = ''.join(lst)
print(answer)
```
