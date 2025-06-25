import csv


def main():
    students = []
    new_students = []
    with open("names.csv","r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append({"name":row["name"], "house":row["house"]})
    
    for student in sorted(students,key=lambda student:student["name"]):#ordena en orden alfabetico los nombres
        last, first = student['name'].split(",")
        last = last.strip()
        first = first.strip()
        houses = student['house']
        new_students.append({"name":first,"last name":last,"house":houses})#lista de diccionarios


        #print(f"{first} ,{last}")
        #print(student['house'])
        

    with open("names_2.csv","w") as f:
        writer = csv.DictWriter(f,fieldnames=["name","last name","house"])
        writer.writeheader()
        for i in new_students:
            writer.writerow(i)
    for i in new_students:
        if i["name"] == "Harry":
            print(i)





main()