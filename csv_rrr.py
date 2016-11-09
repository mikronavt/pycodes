import csv

with open('C:\\1\\prog\\Crimes.csv', newline='') as csvfile:
    creader = csv.reader(csvfile)
    s = {}
    for row in creader:
        date = row[2]
        d = date[6:10:]
        primary_type = row[5]
        if d == "2015":
            s[primary_type] = s.get(primary_type, 0) + 1

print(s)
