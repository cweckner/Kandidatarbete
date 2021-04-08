

import csv
import datetime


new_rows = []

def sun():
    i = 0
    with open(r'sun_data.csv','r') as infile:
        reader = csv.reader(infile, delimiter=",")
        for row in reader:
            i+=1
            date = row[0][:16]
            date = date.replace(" ", "T")
            date = date + "Z"
            power = float(row[1] + ".0") 
            new_rows.append({"date": date, "power": power})

    with open('new_sun_data.csv', 'w') as csvfile:
        fieldnames = ['date', 'power']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for r in new_rows:
            writer.writerow({'date': r['date'], 'power': r['power']})

sun()