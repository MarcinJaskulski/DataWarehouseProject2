class CustomerInfo:
    def __init__(self, row):
        self.Id = int(row[0:9])
        self.firstname = row[9:51].strip()
        self.lastname = row[51:83].strip()
        self.street_address = row[83:193].strip()
        self.district = row[193:233].strip()
        self.voivodship = row[233:283].strip()
        self.postcode = int(row[283:288])
        self.est_income = int(row[288:296])
        self.own_or_rent = row[296]
        self.date = row[297:307]
        if self.own_or_rent == "R":
            self.est_income *= 0.5

    def show(self):
        print(f"CustomerInfo: {self.Id} {self.firstname} {self.lastname} {self.street_address} {self.district} "
              f"{self.voivodship} {self.postcode} {self.est_income} {self.own_or_rent} {self.date}")
