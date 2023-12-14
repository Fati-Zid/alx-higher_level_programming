-- Display the full description of the first_table without DESCRIBE or EXPLAIN
SELECT 
    CONCAT(table_name, '     ', CREATE_TABLE)
FROM 
    information_schema.tables
WHERE 
    table_schema = 'hbtn_0c_0' AND table_name = 'first_table';

