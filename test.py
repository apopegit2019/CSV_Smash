import csv

def test():
    primroles = 'c:/csv/sys_roles1.csv'
    with open(primroles) as primuserroles:
        pusers = csv.DictReader(primuserroles)
        for line in pusers:
            print(line.values())


test()