import csv
from pprint import pprint



with open('Bilkap.csv', newline='') as file:
    reader = csv.reader(file)
    res = list(map(tuple, reader))



pprint(res)


Car = input("Which Car Brand?")

Model = input("Which Car Model?")