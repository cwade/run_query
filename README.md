# run_query
Python 3 script for running a query against and Oracle database and writing the results to a csv file.

Usage::

	run_query.py config.yml sample_query.sql my_output.csv

Connects to database specified in config.yml using username and password. Executes the query and writes it to a file called my_output.csv in the working directory. If the last argument isn't specified, output goes to a file called output.csv in the current working directory.

Dependencies are cx_Oracle (http://cx-oracle.sourceforge.net/) and pandas (http://pandas.pydata.org/). Good instructions for installing cx_Oracle on a Mac are here: http://joelvasallo.com/?p=276.
