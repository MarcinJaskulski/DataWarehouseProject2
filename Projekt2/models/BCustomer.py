class BCustomer:
    def __init__(self, row):
        row = row.replace('\n', '')
        cells = row.split('|')
        self.custid = int(cells[0])
        self.firstname = cells[1].strip()
        self.lastname = cells[2].strip()
        self.street_address = cells[3].strip()
        self.district = cells[4].strip()
        self.voivodship = cells[5].strip()
        self.postcode = int(cells[6].replace('-', ''))

    def show(self):
        print(f"BCustomer: {self.custid} {self.firstname} {self.lastname} {self.street_address} {self.district} "
              f"{self.voivodship} {self.postcode}")
