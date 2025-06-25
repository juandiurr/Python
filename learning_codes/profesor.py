import random
import sys

def main():
    try:
        while True:
            while True:
                level = loop("Level: ")
                if level >= 1 and level <= 3:
                    break
                else:
                    print("Level between 1 and 3")
            
            x1, x2, op = azar(level)
            n = juego(op, x1, x2)
            print(f"Puntos: {n}")
    except KeyboardInterrupt:
        print()
        print("Adios")
        sys.exit()
        
        
        
def juego(xd, x1, x2):
    x1 = str(x1)
    x2 = str(x2)
    n = 10
    while True:
            i = loop(x1 + " " + xd + " "+ x2 + " "+ " = ")
            resultado = eval(f"{x1} {xd} {x2}")
            if i != resultado:
                print("ERR")
                n -= 1
                if n == 0:
                    print("Perdiste")
                    print(f"Resultado: {resultado}")
                    sys.exit()
            else:
                return n
            


def azar(nivel):#devuelve el rango de operacion y un numero azar del 1 al 4

    if nivel == 1:
        r1 = random.randint(-10,10)
        r2 = random.randint(-10,10)
        op = random.randint(1,2)
        
    elif nivel == 2:
        r1 = random.randint(-20,20)
        r2 = random.randint(-20,20)
        op = random.randint(1,4)
        
    elif nivel == 3:
        r1 = random.randint(-100,100)
        r2 = random.randint(-100,100)
        op = random.randint(1,4)
    if op == 1:
        op = "+"
    elif op == 2:
        op = "-"
    elif op == 3:
        op = "*"
    elif op == 4:
        op = "/"
    return r1, r2, op 
































def loop(lol):
    
    while True:
        y = False
        try: 
            x = int(input(lol))
            
            if not y:
                return x
        except ValueError:
            y = True





















if __name__ == "__main__":
    main()