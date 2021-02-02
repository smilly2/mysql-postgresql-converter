# mysql-postgresql-converter

# Fork from https://github.com/lanyrd/mysql-postgresql-converter


## Dump using:
mysqldump --compatible=postgresql --default-character-set=utf8 --skip-lock-tables -r databasename.mysql -u root databasename -p

## converter data:
python db_converter.py databasename.mysql databasename.psql schema

## load data:
psql -f databasename.psql
