-- Here is the SQL file to create the credentials database for CNIT 390.
-- This .sql file is written to be compatible for MySQL in Ubuntu.

DROP TABLE Credentials; -- Drops any credentials table that might already exist.
CREATE TABLE Credentials(
	UserName varchar(10) NOT NULL,
	Password varchar(20) NOT NULL,
	CONSTRAINT credentials_pk PRIMARY KEY(UserName, Password)
);

-- NOTE!!!!!
-- You should ONLY run this .sql file ONCE at the beginning. Otherwise the DROP TABLE will drop the Credentials table along with ALL the data within it.
