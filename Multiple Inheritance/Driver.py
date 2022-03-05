from Person import Person
from Job import Job


class Driver(Person, Job):

    def __init__(self):
        super().__init__()
        self.licenseID = ""
        self.activeUntil = ""
        self.vehicleType = ""

    def setDriver(self, nik, name, gender, sleep, nip, company, position, license, active, type):
        self.setPerson(nik, name, gender, sleep)
        self.setJob(nip, company, position)
        self.licenseID = license
        self.activeUntil = active
        self.vehicleType = type

    def setlicenseID(self, license):
        self.licenseID = license

    def getlicenseId(self):
        return self.licenseID

    def setactiveUntil(self, active):
        self.activeUntil = active

    def getactiveUntil(self):
        return self.activeUntil

    def setvehicleType(self, type):
        self.vehicleType = type

    def getvehicleType(self):
        return self.vehicleType

    def printDriver(self):
        print(">>> DESCRIPTION <<<")
        self.printPerson()
        self.printJob()
        print("License ID : " + self.getlicenseId())
        print("Active : " + self.getactiveUntil())
        print("Vehicle Type : " + self.getvehicleType())
        self.sleep()
