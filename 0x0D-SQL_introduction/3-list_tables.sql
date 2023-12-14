-- List all tables in the specified database (hbtn_0c_0 in this case)
USE hbtn_0c_0;
-- Show tables without using SELECT or SHOW
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0';

