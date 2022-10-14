### 문제
<img src='https://user-images.githubusercontent.com/95834067/195847681-0422e03c-4f8c-4e4b-a661-314d6fca4dcc.png' height='50%' width='50%'>

### 아이디어
* 입양을 아직 보내지 않은 동물들을 알고 싶기 때문에 left join 후 
* where is null 사용
```mysql
SELECT INS.NAME, INS.DATETIME
FROM (ANIMAL_INS AS INS LEFT JOIN ANIMAL_OUTS AS OUTS 
      ON INS.ANIMAL_ID = OUTS.ANIMAL_ID)
WHERE OUTS.ANIMAL_ID IS NULL 
ORDER BY INS.DATETIME 
LIMIT 3;
```
