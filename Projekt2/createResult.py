import numpy as np
import pandas as pd

result_columns = [
    "id", "source", "fname", "lname",
    "street_address", "district", "voivodship",
    "postcode", "preferred", "est_income",
    "own_or_rent", "purchases"
]


def createResultA(join_a_df, TRANSACTION_THRESHOLD):
    returned_ids = join_a_df.loc[join_a_df["transtype"] == "RET"]["returnid"].tolist()
    remove_ret = join_a_df.loc[~join_a_df['returnid'].isin(returned_ids)]
    grouped = remove_ret.groupby("custid")
    a_result = pd.DataFrame()
    for key, value in grouped.groups.items():
        if grouped.get_group(key)["value"].sum() < TRANSACTION_THRESHOLD:
            continue
        customer_info = grouped.get_group(key).iloc[0]
        data = {
            "id": int(customer_info["custid"]),
            "source": "A",
            "fname": customer_info["fname"],
            "lname": customer_info["lname"],
            "street_address": customer_info["street_address"],
            "district": customer_info["district"],
            "voivodship": customer_info["voivodship"],
            "postcode": customer_info["postcode"],
            "preferred": str(customer_info["preferred"]),
            "est_income": None,
            "own_or_rent": "U",
            "purchases": grouped.get_group(key)["value"].sum()
        }
        a_result = a_result.append(data, ignore_index=True)
    return a_result[result_columns]


def createResultB(join_b_df, TRANSACTION_THRESHOLD):
    grouped = join_b_df.groupby("custid")
    b_result = pd.DataFrame()
    for key, value in grouped.groups.items():
        if grouped.get_group(key)["value"].sum() < TRANSACTION_THRESHOLD:
            continue
        customer_info = grouped.get_group(key).iloc[0]
        data = {
            "id": int(customer_info["custid"]),
            "source": "B",
            "fname": customer_info["firstname"],
            "lname": customer_info["lastname"],
            "street_address": customer_info["street_address"],
            "district": customer_info["district"],
            "voivodship": customer_info["voivodship"],
            "postcode": customer_info["postcode"],
            "preferred": "2",
            "est_income": None,
            "own_or_rent": "U",
            "purchases": grouped.get_group(key)["value"].sum()
        }
        b_result = b_result.append(data, ignore_index=True)
    return b_result[result_columns]


def createResultC(customer_info_df, INCOME_THRESHOLD):
    filter_customer_info = customer_info_df.loc[customer_info_df['est_income'] >= INCOME_THRESHOLD]
    filter_customer_info["source"] = "C"
    filter_customer_info["preferred"] = "2"
    filter_customer_info["purchases"] = None
    del filter_customer_info['date']
    mapping = {
        filter_customer_info.columns[0]: 'id',
        filter_customer_info.columns[1]: 'fname',
        filter_customer_info.columns[2]: 'lname',
        filter_customer_info.columns[3]: 'street_address',
        filter_customer_info.columns[4]: 'district',
        filter_customer_info.columns[5]: 'voivodship',
        filter_customer_info.columns[6]: 'postcode',
        filter_customer_info.columns[7]: 'est_income',
        filter_customer_info.columns[8]: 'own_or_rent',
        filter_customer_info.columns[9]: 'source',
        filter_customer_info.columns[10]: 'preferred',
        filter_customer_info.columns[11]: 'purchases',
    }

    filter_customer_info =  filter_customer_info.rename(columns=mapping)
    return filter_customer_info[result_columns]
