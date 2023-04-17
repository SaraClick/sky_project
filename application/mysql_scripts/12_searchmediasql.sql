USE fortywinks;

DELIMITER $$
CREATE PROCEDURE SearchMedia(IN search_term VARCHAR(250))
BEGIN
    SELECT media_id, media_title, type_name, source_name, category_name
    FROM vw_media
    WHERE media_id = search_term
    OR media_title LIKE CONCAT('%', search_term, '%')
    OR type_name LIKE CONCAT('%', search_term, '%')
    OR source_name LIKE CONCAT('%', search_term, '%')
    OR category_name LIKE CONCAT('%', search_term, '%');
END$$
DELIMITER ;

-- SHOW CREATE PROCEDURE SearchMedia;
-- CALL SearchMedia('rain');



-- DROP PROCEDURE SearchMedia;

-- SELECT * FROM media WHERE category_id LIKE '5';

-- SELECT * FROM vw_media WHERE category_name LIKE 'rain';