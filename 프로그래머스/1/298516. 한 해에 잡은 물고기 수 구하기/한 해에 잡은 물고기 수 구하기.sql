SELECT 
    COUNT(DISTINCT ID) AS FISH_COUNT
FROM FISH_INFO
WHERE YEAR(TIME) = 2021
