import pandas as pd


def joinAData(customers, transactions):
    customers_col = ["custid", "fname", "lname", "street_address", "district", "voivodship", "postcode", "preferred"]
    transactions_col = ["transid", "transtype", "transdate", "custid", "prodid", "quantity", "price", "discount",
                        "returnid", "reason", "value"]

    df_customers = pd.DataFrame(
        ([int(x.custid), x.fname, x.lname, x.street_address, x.district, x.voivodship, x.postcode, x.preferred]
         for x in customers), columns=customers_col
    )

    df_transactions = pd.DataFrame(
        ([x.transid, x.transtype, x.transdate, int(x.custid), x.prodid, x.quantity, x.price, x.discount, x.returnid, x.reason, x.value]
         for x in transactions), columns=transactions_col
    )

    return df_customers.merge(df_transactions, on="custid", how="outer")


def joinBData(customers, transactions):
    customers_col = ["custid", "firstname", "lastname", "street_address", "district", "voivodship", "postcode"]
    transactions_col = ["transid", "prodid", "price", "quantity", "transdate", "custid", "value"]

    df_customers = pd.DataFrame(
        ([int(x.custid), x.firstname, x.lastname, x.street_address, x.district, x.voivodship, x.postcode]
         for x in customers), columns=customers_col
    )

    df_transactions = pd.DataFrame(
        ([x.transid, x.prodid, x.price, x.quantity, x.transdate, int(x.custid), x.value]
         for x in transactions), columns=transactions_col
    )

    return df_customers.merge(df_transactions, on="custid", how="outer")


def createDFCustomerInfo(customers_info):
    customers_info_col = ["Id", "firstname", "lastname", "street_address", "district", "voivodship", "postcode", "est_income", "own_or_rent", "date"]

    return pd.DataFrame(
        ([x.Id, x.firstname, x.lastname, x.street_address, x.district, x.voivodship, x.postcode, x.est_income, x.own_or_rent, x.date]
         for x in customers_info), columns=customers_info_col
    )
