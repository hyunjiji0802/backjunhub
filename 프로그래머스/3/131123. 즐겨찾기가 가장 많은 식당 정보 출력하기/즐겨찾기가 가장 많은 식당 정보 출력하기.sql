# 음식종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회
# 음식 종류를 기준으로 내림차순 정렬
# RANK() OVER (PARTITION BY <그룹화할 컬럼> ORDER BY <정렬할 컬럼> DESC)
# WHERE 절에서는 윈도우 함수 결과 Alias 사용 X -> 서브쿼리나 CTE로

#풀이 1. 서브쿼리
# SELECT 
#     tmp.FOOD_TYPE,
#     ri.REST_ID,
#     ri.REST_NAME,
#     ri.FAVORITES
# FROM REST_INFO AS ri
# JOIN ( 
#     SELECT
#         FOOD_TYPE,
#         MAX(FAVORITES) AS MAX_FAV
#     FROM REST_INFO
#     GROUP BY FOOD_TYPE
# ) AS tmp
# ON tmp.FOOD_TYPE = ri.FOOD_TYPE
# AND tmp.MAX_FAV = ri.FAVORITES
# ORDER BY FOOD_TYPE DESC

# 풀이 2. rank()
# 즐겨찾기 많은 순 FOOD_TYPE 별로 확인
# SELECT 
#     FOOD_TYPE,
#     REST_ID,
#     REST_NAME,
#     FAVORITES,
#     RANK() OVER (PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS r
# FROM REST_INFO
# ORDER BY r


SELECT
    FOOD_TYPE,
    REST_ID,
    REST_NAME,
    FAVORITES
FROM (
    SELECT 
        *,
        RANK() OVER (PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS r
    FROM REST_INFO
) AS tmp
WHERE tmp.r = 1
ORDER BY FOOD_TYPE DESC