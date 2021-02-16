import csv

Brand = input("Car Brand?")
Model = input("Car Model?")

with open('Bilkap.csv','r') as infile:
    reader = csv.reader(infile, delimiter=",")
    for row in reader:
        if Brand == row[0]:
            if Model == row[1]:
                print("Battery Capasity" + "\t" + row[2] + "\n" + "ChargePower" + "\t" + row[3])
                break

