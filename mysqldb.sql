CREATE USER 'user' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'MYSQL_DATABASE_ADDRESS';
FLUSH PRIVILEGES;

USE DATABASE;
CREATE TABLE IF NOT EXISTS recipients (
Amt INT, 
GrantOrContributionPurposeTxt TEXT, 
RecipientBusinessName TEXT, 
RecipientFoundationStatusTxt TINYTEXT, 
RecipientPersonNm TEXT, 
RecipientRelationshipTxt TEXT, 
AddressLine1Txt TEXT, 
CityNm TEXT, 
StateAbbreviationCd TEXT, 
ZIPCd TEXT);

UPDATE TABLE SET RecipientBusinessName = replace(RecipientBusinessName, '<BusinessNameLine1Txt>', '');
UPDATE TABLE SET RecipientBusinessName = replace(RecipientBusinessName, '</BusinessNameLine1Txt>', '');
