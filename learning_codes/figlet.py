import sys
from pyfiglet import Figlet
import random

def main():
    
    if len(sys.argv) == 1:
        sys.exit
    elif len(sys.argv) == 2:
        
        figlet = Figlet().getFonts()
        ola = random.randint(1,len(figlet))
        ff = Figlet(font = figlet[ola])
        print(ff.renderText(sys.argv[1]))
        
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "-font" or sys.argv[1] == "--font":
            hola = input("input: ")
            fontt = sys.argv[2]
            ff = Figlet(font = fontt)
            print(ff.renderText(hola))
        else:
            print("para seleccionar font introducir -f")
            sys.exit
main()