import sys

def main():
    
    if len(sys.argv) > 2:
        print("ingrese el nombre de un archivo")
        print(len(sys.argv))
        sys.exit()
    try:
        if sys.argv[1].endswith(".py"):
            
            print(leer(sys.argv[1]))
        else:
            print("archivo debe terminar en .py")
    except IndexError:
        print("introduzca un archivo pendejo")




def leer(i):
    
    n = 0
    try:
        with open(i,"r") as file:
            lines = file.readlines()
            for i in lines:
                i = i.strip()
                if i != "" and not i.startswith("#"):
                    n+=1
        return n
    except FileNotFoundError:
        print("Archivo no existe")
        sys.exit()

main()