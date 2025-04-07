# 개체의 크기를 내름차순으로 정렬했을 때 상위 0% ~ 25% 를 'CRITICAL'
# 26% ~ 50% 를 'HIGH', 51% ~ 75% 를 'MEDIUM', 76% ~ 100% 를 'LOW' 
# 대장균 개체의 ID(ID) 와 분류된 이름(COLONY_NAME)을 출력
# NTILE(N) OVER (PARTITIN BY COL1 ORDER BY COL2)

WITH base AS(
    SELECT
        ID,
        NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS r
    FROM ECOLI_DATA
)

SELECT
    ID,
    CASE
        WHEN r = 1 THEN 'CRITICAL'
        WHEN r = 2 THEN 'HIGH'
        WHEN r = 3 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM base
ORDER BY ID 