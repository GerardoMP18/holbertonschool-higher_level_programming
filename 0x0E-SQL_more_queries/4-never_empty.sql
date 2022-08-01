-- Script that create new table id_not_null but atribute id that default is 1
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
