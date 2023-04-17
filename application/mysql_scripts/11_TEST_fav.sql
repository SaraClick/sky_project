USE fortywinks;

-- drop table favourite;
-- drop table users;


CREATE TABLE users
(user_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
user_email VARCHAR(100) NOT NULL,
user_password VARCHAR(100) NOT NULL,
user_name VARCHAR(100) NOT NULL
);

CREATE TABLE favourite
(media_id INT NOT NULL,
fav BOOLEAN NOT NULL,
user_id INT NOT NULL,
FOREIGN KEY (media_id) REFERENCES media(media_id),
FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users(user_email, user_password, user_name)
VALUES('user1@email.com', 'password1', 'User1'),
('user2@email.com', 'password2', 'User2'),
('user3@email.com', 'password3', 'User3')
;

INSERT INTO favourite(media_id, fav, user_id)
VALUES(14, true, 1),
(40, true, 1),
(41, true, 1),
(42, true, 2),
(43, true, 2),
(44, true, 2)
;

SELECT m.media_id, f.fav, m.media_title
FROM media AS m
INNER JOIN favourite AS f
ON m.media_id = f.media_id
WHERE user_id=1;

UPDATE favourite
SET fav=false
WHERE user_id=1 AND media_id=43;

