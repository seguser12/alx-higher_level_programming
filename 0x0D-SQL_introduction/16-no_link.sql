-- lists all records of the table 'seocnd_table'

SELECT `score`, `name` FROM second_table
    WHERE name != ''
    ORDER BY score DESC;
