from Person import Person
from Job import Job
from Driver import Driver

D = Driver()

print("     +++++++++++++++")
print("     + D r i v e r +")
print("     +++++++++++++++")
print("")

D.setDriver("51335020", "Axel Eldrian", "Male", "7", "12543789450", "Google", "Manager", "A", "2025", "SUV")
D.printDriver()

for i in range(20):
    print("-", end="")

print("")
print("\n")

D.setDriver("65416466", "Edi Gunaedi", "Male", "12", "55daas24a2a", "Microsoft", "Staff", "A", "2023", "Hatchbacl")
D.printDriver()

for i in range(20):
    print("-", end="")

print("")
print("\n")

D.setDriver("2131835", "Alfat mikun", "Female", "8", "528684681", "Shopee", "President", "A", "2030", "Coupe")
D.printDriver()

for i in range(20):
    print("-", end="")

print("")
print("\n")

D.setDriver("4816843", "Ella Ismalina", "Female", "8", "a535335", "Tokopedia", "Directur", "A", "2027", "Sedan")
D.printDriver()

for i in range(20):
    print("-", end="")

print("")
print("\n")

D.setDriver("2115485", "Aldrin Hadiwibowo", "Male", "5", "460618464116", "Permata Bank", "Vice President", "A", "2026", "SUV")
D.printDriver()

for i in range(20):
    print("-", end="")

print("")
print("\n")
