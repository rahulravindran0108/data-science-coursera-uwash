-- select count(*) from (
--	select * from frequency where docid='10398_txt_earn'
--	) x;

--select count(*) from (
--	select * from frequency where docid='10398_txt_earn' and count=1
--) x;

-- select count(*) from (
-- 	select term from frequency where docid='10398_txt_earn' and count=1 union select term from frequency where docid='925_txt_trade' and count=1
-- ) x;

-- select count(*) from (
-- select docid from frequency where term in ('law','legal') group by docid
-- ) x;

-- select count(*) from 
-- (
-- select docid from frequency group by docid having count(*) > 300
-- ) x;

-- select distinct docid from frequency where term in ('transactions') intersect select distinct docid from frequency where term in ('world');

-- SELECT a.row_num, b.col_num, SUM(a.value*b.value)
-- FROM a, b
-- WHERE a.col_num = b.row_num
-- GROUP BY a.row_num, b.col_num;

-- SELECT similarity
-- FROM (
--        SELECT A.docid as firstDoc, B.docid as secondDoc, sum(A.count*B.count) as similarity
--        FROM frequency as A, frequency as B
--        WHERE A.term=B.term
--        GROUP BY A.docid, B.docid
-- )
-- WHERE firstDoc = '10080_txt_crude' and secondDoc = '17035_txt_earn';

SELECT similarity
FROM (
     SELECT B.docid as secondDoc, sum(A.count*B.count) as similarity
     FROM 
        (SELECT *
        FROM frequency
        UNION SELECT 'q' as docid, 'washington' as term, 1 as count 
        UNION SELECT 'q' as docid, 'taxes' as term, 1 as count
        UNION SELECT 'q' as docid, 'treasury' as term, 1 as count) as A,
        (SELECT *
        FROM frequency
        UNION SELECT 'q' as docid, 'washington' as term, 1 as count 
        UNION SELECT 'q' as docid, 'taxes' as term, 1 as count
        UNION SELECT 'q' as docid, 'treasury' as term, 1 as count) as B
     WHERE A.term=B.term and A.docid='q'
     GROUP BY B.docid
)
ORDER BY -similarity
LIMIT 1
;