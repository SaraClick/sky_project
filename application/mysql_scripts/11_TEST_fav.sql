USE fortywinks;

CREATE TABLE favourite
(media_id INT NOT NULL,
fav BOOLEAN NOT NULL,
FOREIGN KEY (media_id) REFERENCES media(media_id)
);


INSERT INTO admins(admin_email, admin_password, admin_status)
VALUES('Mati@fortywinks.com', 'password1', 'active'),
('Mirfat@fortywinks.com', 'password2', 'inactive'),
('Sara@fortywinks.com', 'password3', 'inactive'),
('Pammy@fortywinks.com', 'password4', 'active');
