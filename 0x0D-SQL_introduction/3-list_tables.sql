-- List all tables in the specified database (mysql in this case)
USE mysql;
-- Show tables without using SELECT or SHOW
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'mysql';

