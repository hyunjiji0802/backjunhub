#입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회
#보호 기간이 긴 순
SELECT
    ao.ANIMAL_ID,
    ao.NAME
    # ai.DATETIME,
    # ao.DATETIME
    # DATEDIFF(ao.DATETIME, ai.DATETIME) AS `보호기간`
    # ao.DATETIME - ai.DATETIME
FROM ANIMAL_OUTS AS ao
    INNER JOIN ANIMAL_INS AS ai
    ON ao.ANIMAL_ID = ai.ANIMAL_ID
ORDER BY ao.DATETIME - ai.DATETIME DESC
LIMIT 2