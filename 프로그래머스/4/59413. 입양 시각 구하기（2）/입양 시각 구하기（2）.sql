# 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회
# 시간대 순으로 정렬
# 재귀CTE

# 0시부터 23시까지 모두 나오지 않음
# SELECT 
#     HOUR(DATETIME) AS HOUR,
#     COUNT(*) AS COUNT
# FROM ANIMAL_OUTS
# GROUP BY HOUR(DATETIME)
# ORDER BY 1

# 2. RECURSIVE 로 0시부터 23시 만들기
WITH RECURSIVE tmp AS (
  SELECT 0 AS hour, 0 AS count
  UNION ALL
  SELECT hour + 1, 0
  FROM tmp
  WHERE hour < 23
)
SELECT 
  h.hour,
  IFNULL(COUNT(a.ANIMAL_ID), 0) AS count
FROM tmp h
LEFT JOIN ANIMAL_OUTS a
  ON HOUR(a.DATETIME) = h.hour
GROUP BY h.hour
ORDER BY h.hour;



