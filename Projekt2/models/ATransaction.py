# Tu coś jest nie tak z ilością znaków. Zmniejszyłem proce i discount o jeden
from numpy import NaN


class ATransaction:
    def __init__(self, row):
        self.transid = int(row[0:9])
        self.transtype = row[9:12].strip()
        self.transdate = row[12:18].strip()
        self.custid = int(row[18:26])
        self.prodid = row[26:34].strip()
        self.quantity = self.parse_to_int(row[34:37])
        self.price = int(row[37:43])
        try:
            self.discount = int(row[43:45])
        except ValueError:
            self.discount = 0
        self.returnid = self.parse_to_int(row[45:54])
        self.reason = row[54:84].strip()
        if type(self.price) is int and type(self.quantity) is int:
            self.value = self.price * self.quantity * (1 - self.discount)
        else:
            self.value = 0

    def parse_to_int(self, str):
        str = str.strip()
        if str != '':
            return int(str)
        else:
            return None

    def show(self):
        print(f"ACustomer: {self.transid} {self.transtype} {self.transdate} {self.custid} {self.prodid} "
              f"{self.quantity} {self.price} {self.discount} {self.returnid} {self.reason} {self.value}")
