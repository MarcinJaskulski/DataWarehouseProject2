import pandas as pd

from fileReader import read_a_customers, read_a_transactions, read_b_transactions, read_b_customers, read_customer_info
from createDF import joinAData, joinBData, createDFCustomerInfo
from createResult import createResultA, createResultB, createResultC
import sys
# Zmiennne z zadania



def save_dat_file(data, filename):
    data.to_csv(filename, sep="|", index=False, float_format='%.0f')

def read_arg_from_command_line(arg_index, default_value):
    try:
        return int(sys.argv[arg_index])
    except IndexError:
        return default_value

if __name__ == '__main__':

    INCOME_THRESHOLD=read_arg_from_command_line(1,20000)
    TRANSACTION_THRESHOLD = read_arg_from_command_line(2,500)
    VIP_INCOME = read_arg_from_command_line(3,10900)

    a_customers = read_a_customers()
    a_transactions = read_a_transactions()
    b_transactions = read_b_transactions()
    b_customers = read_b_customers()
    customer_info = read_customer_info()

    # utworzenie DF z plików
    join_a_df = joinAData(a_customers, a_transactions)
    join_b_df = joinBData(b_customers, b_transactions)
    customer_info_df = createDFCustomerInfo(customer_info)

    # filtrowanie A
    res_a = createResultA(join_a_df, TRANSACTION_THRESHOLD)

    # filtrowanie B
    res_b = createResultB(join_b_df, TRANSACTION_THRESHOLD)

    # filtrowanie customers info
    res_c = createResultC(customer_info_df, INCOME_THRESHOLD, VIP_INCOME)

    concat = pd.concat([res_a, res_b, res_c])
    print(concat.count)
    save_dat_file(concat, "result.dat")
