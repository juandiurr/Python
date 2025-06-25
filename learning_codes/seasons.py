from datetime import date
from re import search

            
class MyDate():
    def __init__(self,name):
        d = name
        if not (search(r"^\d{1,4}-\d{1,2}-\d{1,2}$",d)):
            raise ValueError("Invalid date: yyyy-mm-dd")
        
        year,month,day = d.split("-")
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"
    def __sub__(self,other):
        years = abs(self.year - other.year)
        months = abs(self.month - other.month)
        days = abs(self.day - other.day)
        return MyDate(f"{years}-{months}-{days}")
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self,year):
        if int(year) > date.today().year:
            raise ValueError("Inavlid year")
        
        self._year = int(year)
    @property
    def month(self):
        return self._month
    @month.setter
    def month(self,month):
        if int(month) > 12:
            raise ValueError("Inavlid month")
        self._month = int(month)
    @property
    def day(self):
        return self._day
    @day.setter
    def day(self,day):
        if int(day) > 31:
            raise ValueError("Inavlid day")
        self._day = int(day)

def main():
    today_date = MyDate(str(date.today()))
    
    #print(type(today_m))#int
    
    i = input("Date: ")
    
    try:
        m = MyDate(i)
        print(f"Fecha válida: {m.year}-{m.month:02}-{m.day:02}")
    except ValueError as e:
        print("Error:", e)
    resultado = today_date - m
    minutos = resultado.year * 525600 + resultado.month * 43800 + resultado.day * 1440
    print(minutos)
    

    
    

if __name__ == "__main__":
    main()