# 물고기 종류 별로 가장 큰 물고기의 ID, 물고기 이름, 길이
# 물고기의 ID 컬럼명은 ID, 이름 컬럼명은 FISH_NAME, 길이 컬럼명은 LENGTH
# 물고기의 ID에 대해 오름차순 정렬

# 1. 종류 group by
WITH base AS (
    SELECT 
        FISH_TYPE,
        MAX(LENGTH) AS LENGTH
    FROM FISH_INFO
    GROUP BY FISH_TYPE
)


SELECT
    fi.ID,
    fn.FISH_NAME,
    base.LENGTH
FROM base
JOIN FISH_INFO AS fi
    ON base.LENGTH = fi.LENGTH
    AND base.FISH_TYPE = fi.FISH_TYPE
JOIN FISH_NAME_INFO AS fn
    ON base.FISH_TYPE = fn.FISH_TYPE

# SELECT
#     ID,
#     FISH_NAME,
#     LENGTH
# FROM base
# JOIN FISH_NAME_INFO AS fn
#     ON base.FISH_TYPE = fn.FISH_TYPE
# ORDER BY ID