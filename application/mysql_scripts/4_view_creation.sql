-- View creation so we can get the media table with the actual type/source/category name instead of ID
-- NOTEs: 
-- 1. A view is like a virtual table, we use the view to query data so we don't have to be using JOINS on most of the queries
-- 2. There's no point on using OUTER JOINS because all data in our tables is NOT NULL

USE fortywinks;

CREATE VIEW vw_media AS
-- The select is where we set the columns to be shown in the view table. Note that we are using the ALIAS (m/t/s/c) to clarify from which table is each column taken
SELECT m.media_id, m.media_title, m.media_url, 
		m.type_id, t.type_name, 
        m.source_id, s.source_name,
        m.category_id, c.category_name
FROM media AS m
-- To get the type name we need to join type_media to media table
INNER JOIN type_media as t
ON m.type_id = t.type_id
-- To get the source name we need to join source_media to media table
INNER JOIN source_media AS s
ON m.source_id = s.source_id
-- To get the category name we need to join category_media to media table
INNER JOIN category_media AS c
ON m.category_id = c.category_id
;