-- A query that prints the full description of the
-- first_table.
SELECT
    COLUMN NAME AS `Column`,
    DATA_TYPE AS `Data Type`,
    CHARACTER_MAXIMUM_LENGTH AS `Max Length`,
    IS_NULLABLE AS `Nullable`,
    COLUMN_DEFAULT AS `Default value`,
    COLUMN_KEY AS `Key`,
    EXTRA AS `Extra`
FROM
    INFORMATION_SCHEMA.COLUMNS
WHER
    TABLE_SCHEMA = 'hbtn_0c_0'
    AND TABLE_NAME = 'first_table';
