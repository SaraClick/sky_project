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


-- GetUrl will retrieve the URLs matching the type and category provided (unique values only)
-- type_selection: string passed on with the user selection 
-- category_selection: string passed on with the user selection 
DELIMITER $$
CREATE PROCEDURE GetUrl(IN type_selection VARCHAR(50), category_selection VARCHAR(100))
BEGIN
-- DICSTICT will ensure that only unique values are included in our column data
	SELECT DISTINCT media_url
    FROM vw_media
    WHERE type_name=type_selection AND category_name=category_selection;
	
END$$
DELIMITER ; 

-- Uncomment to test
-- CALL GetUrl('sound', 'instrumental');


