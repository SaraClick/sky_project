CREATE DATABASE FortyWinks;

USE FortyWinks;

-- creation of tables for the ddbb
 
CREATE TABLE type_media
(type_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
type_name VARCHAR(50) NOT NULL
);

CREATE TABLE source_media
(source_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
source_name VARCHAR(50) NOT NULL
);

CREATE TABLE category_media
(category_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
category_name VARCHAR(100) NOT NULL
);

-- media table uses foreign keys from source, catergory and type 
-- media_url to be used in the iframe src 

CREATE TABLE media
(media_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
media_title VARCHAR(250) NOT NULL,
media_url VARCHAR(250) NOT NULL,
type_id INT NOT NULL,
source_id INT NOT NULL,
category_id INT NOT NULL,
FOREIGN KEY (type_id) REFERENCES type_media(type_id),
FOREIGN KEY (source_id) REFERENCES source_media(source_id),
FOREIGN KEY (category_id) REFERENCES category_media(category_id)
);







