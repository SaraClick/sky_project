use fortywinks;

-- Stored Procedure to insert data into type_media
DELIMITER $$
CREATE PROCEDURE InsertType(IN type_name VARCHAR(50))
BEGIN
	INSERT INTO type_media(type_name)
	VALUES (type_name);
END$$
DELIMITER ; 

-- Stored Procedure to insert data into source_media
DELIMITER $$
CREATE PROCEDURE InsertSource(IN source_name VARCHAR(50))
BEGIN
	INSERT INTO source_media(source_name)
	VALUES (source_name);
END$$
DELIMITER ; 

-- Stored Procedure to insert data into category_media
DELIMITER $$
CREATE PROCEDURE InsertCategory(IN category_name VARCHAR(100))
BEGIN
	INSERT INTO category_media(category_name)
	VALUES (category_name);
END$$
DELIMITER ; 


-- Stored Procedure to insert data into media
DELIMITER $$
CREATE PROCEDURE InsertMedia(IN media_title VARCHAR(250), media_url VARCHAR(250), type_id INT, source_id INT, category_id INT)
BEGIN
	INSERT INTO media(media_title, media_url, type_id, source_id, category_id)
	VALUES (media_title, media_url, type_id, source_id, category_id);
END$$
DELIMITER ; 