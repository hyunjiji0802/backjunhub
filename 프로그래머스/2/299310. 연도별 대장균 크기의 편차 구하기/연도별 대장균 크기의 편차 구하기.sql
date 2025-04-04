# SELECT 
#     YEAR(DIFFERENTIATION_DATE) AS YEAR,
#     MAX(SIZE_OF_COLONY) - SIZE_OF_COLONY AS YEAR_DEV,
#     ID
# FROM ECOLI_DATA
# GROUP BY 

SELECT 
    tmp.YEAR,
    tmp.MAX_SIZE - SIZE_OF_COLONY AS YEAR_DEV,
    ID
FROM ECOLI_DATA
JOIN (
    SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR,
        MAX(SIZE_OF_COLONY) AS MAX_SIZE
    FROM ECOLI_DATA
    GROUP BY YEAR(DIFFERENTIATION_DATE)
) AS tmp
ON YEAR(DIFFERENTIATION_DATE) = tmp.YEAR
ORDER BY YEAR ASC, YEAR_DEV ASC
