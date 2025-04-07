# 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로를 조회
# 첨부파일 경로는 FILE ID를 기준으로 내림차순 정렬
# 기본적인 파일경로는 /home/grep/src/ , 게시글 ID를 기준으로 디렉토리가 구분
# 파일이름은 파일 ID, 파일 이름, 파일 확장자로 구성

#1.조회수가 가장 높은 중고거래 게시물 조회
# SELECT *
# FROM USED_GOODS_BOARD
# ORDER BY VIEWS
# LIMIT 1

#2. left join
SELECT 
    CONCAT('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE AS uf
WHERE uf.BOARD_ID = (
    SELECT BOARD_ID
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1
)
ORDER BY FILE_ID DESC


