use fortywinks;

-- created table for admin login and admin status

CREATE TABLE admins (
admin_id INT AUTO_INCREMENT PRIMARY KEY,
admin_username VARCHAR(50) NOT NULL, 
admin_password VARCHAR(50) NOT NULL,
admin_status ENUM('active', 'inactive') NOT NULL
);

-- drop table admins;

-- CREATE TABLE admin_status (
-- admin_id INT PRIMARY KEY,
-- status VARCHAR(10) NOT NULL,
-- FOREIGN KEY (admin_id) REFERENCES admins(admin_id)
-- );
