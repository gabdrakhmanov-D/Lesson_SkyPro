import pandas as pd
import csv

def csv_file_reader(path_to_file: str) -> list:
    with open(path_to_file, encoding='utf-8') as file:
        csv_data = csv.DictReader(file, delimiter=';')
        list_transactions = []
        for row in csv_data:
            list_transactions.append(row)
        return list_transactions

def excel_file_reader():
    pass

if __name__ == '__main__':
    a=csv_file_reader('../data/transactions.csv')
    print(a)