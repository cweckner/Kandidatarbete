import csv

Brand = input("Car Brand?")
Model = input("Car Model?")
def CARSPEC(b,m):
    with open('Bilkap.csv','r') as infile:
        reader = csv.reader(infile, delimiter=",")
        for row in reader:
            if b == row[0]:
                if m == row[1]:
                    return "Battery Capasity" + "\t" + row[2] + "\n" + "ChargePower" + "\t" + row[3]

print(CARSPEC(Brand,Model))
