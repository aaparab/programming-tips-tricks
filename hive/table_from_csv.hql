-- Create ORC table from a CSV file. 

-- Location of csv file (including database): 
--     /home/abhi/mydatabase.db/mycsvfile.csv



-- Create empty table:
CREATE TABLE IF NOT EXISTS mydatabase.mytable_tmp
(
      col1 BIGINT
    , col2 INT
    , col3 STRING
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','



-- Create temporary table using csv file data
LOAD DATA INPATH '/home/abhi/mydatabase.db/mycsvfile.csv'
    OVERWRITE INTO TABLE mydatabase.mytable_tmp
    


-- Create empty ORC table
CREATE TABLE IF NOT EXISTS mydatabase.mytable
(
      col1 BIGINT
    , col2 INT
    , col3 STRING
)
STORED AS ORC



-- Copy data from temporary table into ORC table
INSERT INTO TABLE mydatabase.mytable SELECT * FROM mydatabase.mytable_tmp



-- Delete temporary table 
-- NOTE: ALSO DELETES CSV FILE! 
DROP TABLE IF EXISTS mydatabase.mytable_tmp
