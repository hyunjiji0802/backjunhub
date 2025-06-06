# 세대별 "자식이 없는" 개체의 수 와 세대번호 출력

# 재귀CTE
WITH RECURSIVE tmp AS (
  SELECT 
    1 AS GENERATION,
    ID,
    PARENT_ID
  FROM ECOLI_DATA
  WHERE PARENT_ID IS NULL

  UNION ALL
  
  SELECT  
    tmp.GENERATION + 1,
    ECOLI_DATA.ID,
    ECOLI_DATA.PARENT_ID
  FROM ECOLI_DATA
  JOIN tmp
  WHERE ECOLI_DATA.PARENT_ID = tmp.ID
),

# SELECT * FROM tmp


# SELECT
#     t1.ID,
#     t2.ID AS CHILDREN_ID,
#     t1.GENERATION
# FROM tmp t1
# JOIN tmp t2
# ON t1.ID != t2.PARENT_ID
# AND t1.GENERATION + 1 = t2.GENERATION

# 자식 있는 ID
HAS_CHILDREN AS (
SELECT
    t1.ID,
    t2.ID AS CHILDREN_ID,
    t1.GENERATION
    # COUNT(DISTINCT t1.ID) AS COUNT,
    # t1.GENERATION
FROM tmp t1
JOIN tmp t2
ON t1.ID = t2.PARENT_ID
AND t1.GENERATION + 1 = t2.GENERATION
# GROUP BY GENERATION
ORDER BY GENERATION
)

SELECT
    COUNT(DISTINCT ID) AS COUNT,
    GENERATION
FROM tmp
WHERE ID NOT IN (SELECT ID FROM HAS_CHILDREN)
GROUP BY GENERATION
    