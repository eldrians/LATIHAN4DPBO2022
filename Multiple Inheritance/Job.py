class Job:

    def __init__(self):
        self.NIP = ""
        self.companyName = ""
        self.position = ""

    def setJob(self, nip, company, position):
        self.NIP = nip
        self.companyName = company
        self.position = position
    
    def setNIP(self, nip):
        self.NIP = nip

    def getNIP(self):
        return self.NIP

    def setcompanyName(self, company):
        self.companyName = company

    def getcompanyName(self):
        return self.companyName

    def setposition(self, position):
        self.position = position

    def getposition(self):
        return self.position

    def printJob(self):
        print(">>> DESCRIPTION <<<")
        print("NIP : " + self.getNIP())
        print("Company : " + self.getcompanyName())
        print("Position : " + self.getposition())