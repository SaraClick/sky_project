USE fortywinks;

CREATE TABLE contactform (
  contact_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  surname VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  message TEXT NOT NULL,
  submission_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- drop table contactform;