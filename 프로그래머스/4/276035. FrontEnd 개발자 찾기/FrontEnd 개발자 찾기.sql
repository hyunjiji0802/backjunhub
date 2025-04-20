# Front End 스킬을 가진 개발자의 정보를 조회
# 조건에 맞는 개발자의 ID, 이메일, 이름, 성을 조회


# 처음 코드 (오답)
# SELECT 
#     ID,
#     EMAIL,
#     FIRST_NAME,
#     LAST_NAME
# FROM DEVELOPERS d
# # & 연산했을때 FRONT END 나온 값이 SKILLCODES의 front end에 코드 있는 지 비교
# WHERE ((d.SKILL_CODE & (
#   SELECT CODE
#   FROM SKILLCODES
#   WHERE CATEGORY = 'Front End'
# )) IN (SELECT CODE FROM SKILLCODES WHERE CATEGORY = 'Front End'))
# OR ((d.SKILL_CODE & (
#   SELECT CODE
#   FROM SKILLCODES
#   WHERE CATEGORY = 'Front End'
# )) = (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End'))
# ORDER BY ID



SELECT 
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM DEVELOPERS d
# & 연산했을때 FRONT END 나온 값이 0이 아니면 됨
WHERE (d.SKILL_CODE & (
  SELECT SUM(CODE)
  FROM SKILLCODES
  WHERE CATEGORY = 'Front End'
)) != 0
ORDER BY ID


