# 일부 데이터가 유실
# 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회


SELECT 
    ao.ANIMAL_ID,
    ao.NAME
FROM ANIMAL_OUTS AS ao
LEFT OUTER JOIN ANIMAL_INS AS ai
ON ao.ANIMAL_ID = ai.ANIMAL_ID
WHERE ai.ANIMAL_ID IS NULL