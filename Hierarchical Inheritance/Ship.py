from Vehicle import Vehicle


class Ship(Vehicle):

    def __init__(self):
        super().__init__()
        self.Type = ""
        self.Age = ""
        self.CountryOfManufacture = ""

    def setShip(self, brand, fueltype, passenger, speed, age, type, COM):
        self.setVehicle(brand, fueltype, passenger, speed)
        self.Age = age
        self.Type = type
        self.CountryOfManufacture = COM

    def setAge(self, age):
        self.Age = age

    def getAge(self):
        return self.Age

    def setType(self, type):
        self.Type = type

    def getType(self):
        return self.Type

    def setCountryOfManufacture(self, manufacture):
        self.CountryOfManufacture = manufacture

    def getCountryOfManucufacture(self):
        return self.CountryOfManufacture

    def printShip(self):
        print(">>> SPECIFICATION <<<")
        print("Type : " + self.getType())
        print("Age : " + self.getAge())
        print("Country Of Manufacture : " + self.getCountryOfManucufacture())
        self.DataPrint()
        print("\n")
        self.Move()

        