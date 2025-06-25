def main():
    while True:
        try:
            x = iput()
            print(f"{x:.2%}")
            break
        except ErrorLoco:
            pass

    

def iput():
    x = input("Fuell: ")
    
    #x1 = x.replace("/","")
    if not x.replace("/","").isalnum():
        print("no es fraccion")
        raise ErrorLoco()
    else:
        x = x.split("/")

        try:
            x_i = [int(i) for i in x]
            if x_i[0] > x_i[1]:
                    print("Fraccion invalida")
                    raise ErrorLoco()
        except (ValueError, IndexError):
            print("Debe ingresar una fraccion")
            raise ErrorLoco()
        except ZeroDivisionError:
            print("Fraccion dividida entre 0")
            raise ErrorLoco()
        else:
            return x_i[0]/x_i[1]
            

        
class ErrorLoco(Exception):
    pass
        
    

main()