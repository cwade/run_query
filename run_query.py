#! /usr/bin/env python3

import cx_Oracle
import getpass
import sys
import yaml
from pandas import DataFrame

config_file = sys.argv[1]
query_file = sys.argv[2]
if len(sys.argv) > 3:
	output_file = sys.argv[3]
else:
	output_file = "output.csv"


with open(config_file, 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

user = cfg['database']['username']
if 'password' in cfg['database']:
	pwd = cfg['database']['password']
else:
	pwd = getpass.getpass('Database password: ')
host = cfg['database']['host']

with open(query_file) as q:
	query = q.read()

con = cx_Oracle.connect("{}/{}@{}".format(user, pwd, host))
cur = con.cursor()
cur.execute(query)
r = cur.fetchall()
cols = [n[0] for n in cur.description]
cur.close()
con.close()

data = DataFrame.from_records(r, columns=cols)

with open(output_file, 'w') as dataset:
	data.to_csv(dataset, index=False)
