-- Stored Procedures to be used in our back-end

USE fortywinks;

-- GetType will retrieve the unique type_names within our type_media table
DELIMITER $$
CREATE PROCEDURE GetType()
BEGIN
-- DICSTICT will ensure that only unique values are included in our column data
	SELECT DISTINCT type_name
    FROM type_media;
END$$
DELIMITER ; 

-- Uncomment to test
-- CALL GetType();


-- GetCategory will retrieve the unique category_names within our category_media table
DELIMITER $$
CREATE PROCEDURE GetCategory()
BEGIN
-- DICSTICT will ensure that only unique values are included in our column data
	SELECT DISTINCT category_name
    FROM category_media;
END$$
DELIMITER ; 

-- Uncomment to test
-- CALL GetCategory();


-- GetUrl will retrieve the URL to be used in the SRC of HTML given a type and category selected by users





