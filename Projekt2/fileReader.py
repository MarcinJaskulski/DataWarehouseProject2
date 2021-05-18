# funkcje do czytania poszczególnych plików
from models.ACustomer import ACustomer
from models.ATransaction import ATransaction
from models.BCustomer import BCustomer
from models.BTransaction import BTransaction
from models.CustomerInfo import CustomerInfo


def read_a_customers():
    rows = []
    with open('./zadanie_politechnika/a-customers.txt', encoding='iso-8859-2') as fp:
        lines = fp.readlines()
        for line in lines:
            rows.append(ACustomer(line))
    return rows


def read_a_transactions():
    rows = []
    with open('./zadanie_politechnika/a-transactions.txt', encoding='iso-8859-1') as fp:
        lines = fp.readlines()
        for line in lines:
            rows.append(ATransaction(line))
    return rows


def read_b_customers():
    rows = []
    with open('./zadanie_politechnika/b-customers.dat', encoding='windows-1250') as fp:
        lines = fp.readlines()
        for line in lines:
            rows.append(BCustomer(line))
    return rows


def read_b_transactions():
    rows = []
    with open('./zadanie_politechnika/b-transactions.dat', encoding='iso-8859-1') as fp:
        lines = fp.readlines()
        for line in lines:
            rows.append(BTransaction(line))
    return rows


def read_customer_info():
    rows = []
    with open('./zadanie_politechnika/cust-info.dat', encoding='ibm037') as fp:
        lines = chunk_string(fp.read(), 307)
        for line in lines:
            # print(line.encode('ibm037').decode('utf-8'))
            # print(line.encode('iso-8859-2'))
            rows.append(CustomerInfo(line))
    # print(rows[193].show())
    return rows


def chunk_string(str, length):
    rows = []
    for i in range(0, len(str), length):
        rows.append(str[0+i:length+i])
    return rows
