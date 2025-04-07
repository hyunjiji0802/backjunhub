# 더 이상 업그레이드할 수 없는 아이템의 아이템 ID(ITEM_ID), 아이템 명(ITEM_NAME), 아이템의 희귀도(RARITY)
# 아이템 ID를 기준으로 내림차순 정렬
# 계층 쿼리
SELECT 
    ii.ITEM_ID,
    ii.ITEM_NAME,
    ii.RARITY
FROM ITEM_INFO ii
LEFT JOIN ITEM_TREE it
ON ii.ITEM_ID = it.PARENT_ITEM_ID
WHERE it.ITEM_ID IS NULL
ORDER BY ii.ITEM_ID DESC