class ACustomer:
    def __init__(self, row):
        self.custid = int(row[0:8])
        self.fname = row[8:28].strip()
        self.lname = row[28:53].strip()
        self.street_address = row[53:143].strip()
        self.district = row[143:173].strip()
        self.voivodship = row[173:193].strip()
        self.postcode = int(row[193:198])
        self.preferred = int(row[198])

    def show(self):
        print(f"ACustomer: {self.custid} {self.fname} {self.lname} {self.street_address} {self.district} "
              f"{self.voivodship} {self.postcode} {self.preferred}")
