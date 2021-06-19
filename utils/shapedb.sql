CREATE TABLE test
(title varchar(200), contributors varchar(200), iswc varchar(11));

COPY test FROM 'D:/dev/BMAT/SingleView/utils/works_single_view_test/works_metadata.csv' WITH (FORMAT csv);