
def main():
    shorten("hola")

def shorten(inpu):
    #inpu = input("Input: ")
    retorno = []
    if vocales(inpu) == -1:
        print(inpu)
        return inpu
        
    else:
        nuevo = inpu
        retorno = vocales(inpu)
        for i in retorno:
            nuevo = nuevo.replace(i, "")
        print(nuevo)
        return nuevo

def vocales(n):
    no = 0
    vocales = "aeiouAEIOU"
    o = 0
    retorno = []
    for i in n:
        #print(i, end = ", ")
        if i in vocales:
            no = 1
            if i not in retorno:
                retorno.append(i)
        
                
    if no == 1:
        return retorno
    else: 
        return -1
        
            

if __name__ == "__main__":
    main()