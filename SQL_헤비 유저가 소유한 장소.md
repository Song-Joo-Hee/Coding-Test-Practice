### 문제
* 프로그래머스
<img src='https://user-images.githubusercontent.com/95834067/195854899-d532c07f-2ad5-4895-8d37-f42ee1a48905.png' height='50%' width='50%'>

```mysql
SELECT PLACES.ID, PLACES.NAME, PLACES.HOST_ID
FROM PLACES, (SELECT HOST_ID, COUNT(ID) cnt FROM PLACES GROUP BY HOST_ID HAVING cnt >= 2) HEAVY_USER
WHERE PLACES.HOST_ID = HEAVY_USER.HOST_ID
ORDER BY PLACES.ID
```

* 다른 풀이를 참고하니 WHERE IN 절로 더 간단하게 풀이하였다.

```mysql
SELECT *
FROM PLACES
WHERE HOST_ID IN (SELECT HOST_ID FROM PLACES GROUP BY HOST_ID HAVING COUNT(ID) >= 2)
ORDER BY PLACES.ID
```

