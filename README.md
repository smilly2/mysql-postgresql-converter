# mysql-postgresql-converter

# Fork from https://github.com/lanyrd/mysql-postgresql-converter
### support postgres schema
### fixed mysql ddl 'comment' converter error

## Dump using:
mysqldump --compatible=postgresql --default-character-set=utf8 --skip-lock-tables -r databasename.mysql -u root databasename -ppwd

## converter data:
python db_converter.py databasename.mysql databasename.psql schema

## load data:
psql -f databasename.psql
