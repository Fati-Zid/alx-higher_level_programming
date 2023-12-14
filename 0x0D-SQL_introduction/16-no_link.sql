-- List all records of the second_table, excluding rows without a name value
SELECT * FROM hbtn_0c_0.second_table WHERE name IS NOT NULL ORDER BY score DESC;

