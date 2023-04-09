-- Stored Procedures to be used in our back-end update and delete

USE fortywinks;

-- UpdateUrl
DELIMITER $$
CREATE PROCEDURE UpdateUrl(IN media_id_update INT, new_Url VARCHAR(250))
BEGIN
	UPDATE media
    SET media_Url = new_Url
    WHERE media_id = media_id_update;
END$$
DELIMITER ; 

-- Uncomment to test
-- CALL UpdateUrl(1, "https://youtu.be/Q6MemVxEquE");


-- DeleteMedia
DELIMITER $$
CREATE PROCEDURE DeleteMedia(IN media_id_delete INT)
BEGIN
	DELETE FROM media
    WHERE media_id = media_id_delete;
END$$
DELIMITER ; 

-- Uncomment to test
-- CALL DeleteMedia(19);