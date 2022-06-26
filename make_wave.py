#!/usr/bin/python3

import sys
import csv
import random
import string

# Date, Amount, Description
def wave_output(transactions):
    ofile_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=40))
    count = 0
    for k in transactions.keys():
        ofile = f'{ofile_name}.{k.lower()}.wave.csv'
        print (ofile)
        with open(ofile, 'w') as csvfile:
            headers = ['Date', 'Description', 'Amount']
            wavewriter = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=headers)            
            wavewriter.writeheader()
            for r in transactions[k]:
                gross = f"{float(r['Gross ']):.2f}"
                wavewriter.writerow({'Date': r['Date'], 'Description': r['Name'] + ' ' + r['Description'], 'Amount': gross})
                if r['Fee '] != '0':
                    fees = f"{float(r['Fee ']):.2f}"
                    wavewriter.writerow({'Date': r['Date'], 'Description': "PayPal Fee", 'Amount': fees})

def make_wave(input_file):
    transactions = {}
    with open(input_file) as f:
        infile = csv.DictReader(f)
        for r in infile:
            if not r['Currency'] in transactions:
                transactions[r['Currency']] = []
            transactions[r['Currency']].append(r)
    wave_output(transactions)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'{sys.argv[0]} paypal.csv')
        sys.exit(-1)
    make_wave(sys.argv[1])
