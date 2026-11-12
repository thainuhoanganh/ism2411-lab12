'''
1. Excel provides a visual spreadsheet interface that is fast for manual inspection and 
quick manual edits. Python automates repetitive data transformations without manual clicks, 
handles datasets larger than Excel's row limit, and ensures reproductible results through version-controlled code. 

2. An e-commerce order processing or payment system benefits from an append-mode log file. 
Each completed transaction appends a timestamped record to the end of the file without overwriting 
prior entries, creating a reliable audit trail for financial reconcilliation and debugging. 
'''

import csv
from datetime import datetime

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


print('--- Exercise 3 ---')

with open(SALES_FILE, 'r') as f:
    reader = csv.reader(f)
    header = next(reader) # next() returns the next item from the iterator, which is the header row in this. 
    print(f'Header: {header}')
    for row in reader:
        print(row)


print('--- Exercise 4 ---')
total_revenue = 0

with open (SALES_FILE, 'r') as f: 
    reader = csv.reader(f)
    next(reader) # skip the header row
    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        total_revenue += total
        print(f'{product}: {quantity} units x ${price:.2f} = ${total:.2f}')

print(f'Total Revenue: ${total_revenue:.2f}')


print('--- Exercise 5 ---')
rows_read = 0
high_value = []

with open(SALES_FILE, 'r') as f:
    reader = csv.reader(f)
    next(reader) #skip header
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        if total > 100:
            high_value.append([product, f'{price:.2f}', quantity, f'{total:.2f}'])

with open (CLEANED_FILE, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Product', 'Price', 'Qty', 'Total'])
    for row in high_value:
        writer.writerow(row)
        print(row)

print(f'Original rows: {rows_read}, rows written to cleaned file: {len(high_value)}')


print('--- Exercise 6 ---')
dict_total = 0

with open (SALES_FILE, 'r') as f: 
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row['price'])
        quantity = int(row['quantity'])
        total = price * quantity
        dict_total += total 
        print(f'{row['product']}: {quantity} units x ${price:.2f} = ${total:.2f}')

print(f'Total Revenue: ${dict_total:.2f}')


print('--- Exercise 7 ---')
summary = {}

with open(SALES_FILE, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
            product = row['product']
            total = float(row['price']) * int(row['quantity'])
            summary[product]= summary.get(product, 0) + total

for product in sorted(summary.keys()):
    print(f'{product}: ${summary[product]:.2f}')


print('--- Exercise 8 ---')
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open(LOG_FILE, 'a') as f: 
    f.write(f'{timestamp} - Total Revenue: ${total_revenue:.2f}\n')

entries = 0
with open(LOG_FILE, 'r') as f:
    for line in f:
        entries += 1
        print(line.strip())

print(f'Log entries so far: {entries}')

