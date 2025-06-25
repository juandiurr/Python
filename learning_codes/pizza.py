from tabulate import tabulate
import csv

def main():
    row = []
    with open("sicilian.csv") as f:
        reader = csv.DictReader(f)
        for l in reader:
            row.append({"Sicilian Pizza":l["Sicilian Pizza"],"Small":l["Small"],"Large":l["Large"]})
   # for i in row:
    #    print(f"{i["Sicilian Pizza"]}, {i["Small"]}, {i["Large"]}")
    print(row)
    print(tabulate(row))

        
    


main()