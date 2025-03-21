# SELECT 
#     COUNT(CASE
#             WHEN n.FISH_NAME = 'BASS' THEN TRUE
#             WHEN n.FISH_NAME = 'SNAPPER' THEN TRUE
#             ELSE FALSE
#         END)AS FISH_COUNT
# FROM FISH_INFO AS f
# JOIN FISH_NAME_INFO AS n ON f.FISH_TYPE = n.FISH_TYPE



SELECT
    COUNT(*) AS FISH_COUNT
    # COUNT(CASE
    #         WHEN n.FISH_NAME = 'BASS' THEN TRUE
    #         WHEN n.FISH_NAME = 'SNAPPER' THEN TRUE
    #         ELSE FALSE
    #     END)AS FISH_COUNT
FROM FISH_INFO AS f
JOIN FISH_NAME_INFO AS n ON f.FISH_TYPE = n.FISH_TYPE
WHERE n.FISH_NAME IN ('BASS', 'SNAPPER')