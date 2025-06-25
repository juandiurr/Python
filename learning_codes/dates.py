meses = {
    "January" : 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
def main():
    date = input("Date: ")
    form = formato(date)
    if form == 1:
        mes, dia, ano = date.split("/")

    elif form == 2:
        mes, dia, ano = date.split("-")
        
    elif form == 3:
        mes, dia, ano = date.split(" ")# September 8, 1988
        for i in meses:
            if mes in i:
                mes = meses[i]

        dia = dia.replace(",","")
    print(f"{ano}-{int(mes):02}-{int(dia):02}")
        

    
def formato(ou):
    for i in ou:
        if i == "/":
            return 1
        elif i == "-":
            return 2
    return 3
main()