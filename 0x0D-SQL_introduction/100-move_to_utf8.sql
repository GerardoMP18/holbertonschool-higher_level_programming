-- Script that converrts hbtn_0c_0 database to UFT8
ALTER DATABASE hbtn_0c_0
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table
	CONVERT TO CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table
	CHANGE name name VARCHAR(256)
	CHARACTER SET utf8mb4
	COLLATE utf8mb4_unicode_ci;
