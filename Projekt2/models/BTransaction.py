# Tu coś jest nie tak z ilością znaków. Zmniejszyłem proce i discount o jeden
from numpy import NaN


class BTransaction:
    def __init__(self, row):
        cells = row.split(',')
        self.transid = int(cells[0])
        self.prodid = cells[1].strip()
        self.price = int(cells[2])
        self.quantity = int(cells[3])
        self.transdate = cells[4].strip()
        self.custid = int(cells[5])
        if type(self.price) is int and type(self.quantity) is int:
            self.value = self.price * self.quantity
        else:
            self.value = 0

    def show(self):
        print(f"ACustomer: {self.transid} {self.prodid} {self.price} {self.quantity} {self.transdate} {self.custid} {self.value}")
