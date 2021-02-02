import sys
import os
if len(sys.argv) > 0:
    schema = sys.argv[1]

os.system('mysqldump --compatible=postgresql --default-character-set=utf8 --skip-lock-tables -r'+schema+'.mysql -uroot -p*** --databases '+ schema)

os.system('python db_converter.py '+schema+'.mysql '+schema+'.psql '+schema)
