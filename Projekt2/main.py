from fileReader import read_a_customers, read_a_transactions, read_b_transactions, read_b_customers, read_customer_info
from models.ACustomer import ACustomer
from models.ATransaction import ATransaction

# Zmiennne z zadania
INCOME_THRESHOLD = 200000
TRANSACTION_THRESHOLD = 500
VIP_INCOME = 10900

if __name__ == '__main__':
    a_customers = read_a_customers()
    a_transactions = read_a_transactions()
    b_transactions = read_b_transactions()
    b_customers = read_b_customers()
    customer_info = read_customer_info()

    for a in customer_info:
        a.show()


