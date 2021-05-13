# Tu coś jest nie tak z ilością znaków. Zmniejszyłem proce i discount o jeden
class ATransaction:
    def __init__(self, row):
        self.transid = int(row[0:9])
        self.transtype = row[9:12].strip()
        self.transdate = row[12:18].strip()
        self.custid = int(row[18:26])
        self.prodid = row[26:34].strip()
        self.quantity = self.parse_to_int(row[34:37])
        self.price = int(row[37:43])
        self.discount = int(row[42:45])
        self.returnid = self.parse_to_int(row[45:54])
        self.reason = row[54:84].strip()

    def parse_to_int(self, str):
        str = str.strip()
        if str != '':
            return int(str)
        else:
            return None

    def show(self):
        print(f"ACustomer: {self.transid} {self.transtype} {self.transdate} {self.custid} {self.prodid} "
              f"{self.quantity} {self.price} {self.discount} {self.returnid} {self.reason}")
