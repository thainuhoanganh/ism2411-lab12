import csv
from datatime import datatime

SALES_FILE = 'data/sales.csv'
CLEANED_FILE = 'data/cleaned.csv'
LOG_FILE = 'data/run_log.txt'

print('--- Exercise 1 ---')
with open (SALES_FILE, 'r') as f:
    print(f'Opened {SALES_FILE}.')

print('--- Exercise 2 ---')
with open(SALES_FILE, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open(LOG_FILE, 'a') as f:
    f.writer('one run\n')