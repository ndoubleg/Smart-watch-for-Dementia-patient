-- Here is the .sql to create the database for the data being gathered from the map API.
-- This .sql file is written to be compatible for MySQL

DROP TABLE SmartWatch; -- Drops the table if it already exists.

-- creating the table
CREATE TABLE SmartWatch(
	longitude varchar(10) NOT NULL,
	latitude varchar(10) NOT NULL,
	CONSTRAINT smartwatch_pk PRIMARY KEY(longitude, latitude)
);

-- Note!!!!!
-- Only run this once or else you will lose ALL of the data within this database.
