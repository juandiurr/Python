import random
import msvcrt
import sys
import base64
import os
entrada = "palabras.txt"
salida = "palabras_lista.txt"
ACTUALIZAR_LISTA = False
NUMERO_DE_PISTAS = 3
documento = "palabras_lista.txt"
palabra = ""
intentos = 0
p = []
n_pistas = NUMERO_DE_PISTAS + 1
pos_pistas = []
enable_pistas = False
intentos_restantes = 0

def input_limitado(max_len, auto=None):
    global p
    global n_pistas
    if auto is not None:
        print(auto)
        return auto[:max_len]
    texto = ""
    
    while True:
        tecla = msvcrt.getwch()
        # CTRL + C
        if tecla == "\x03":
            limpiar_archivo("guardado.txt")
            print(f"\nPerdedor, te rendiste a los {intentos} intentos")
            if sys.argv[1] == "continuar":
                print("La palabra era: ", pal)
            else:
                print("La palabra era: ", palabra[0])
            sys.exit()
        elif tecla == "\r":  # ENTER
            print()
            break
        
        elif tecla == "\x01":  # CTRL + A
            if(enable_pistas):
                if n_pistas != 0:
                    n_pistas-=1
                if sys.argv[1] == "continuar":
                    dar_pista(len(pal))
                else:
                    dar_pista(len(palabra[0]))
            else:
                print("        Pistas inhabilitadas")
        elif tecla == "\x13": #CTRL S
            limpiar_archivo("guardado.txt")
            limpiar_archivo("pos.txt")
            if sys.argv[1] == "continuar":
                encode = base64.b64encode(pal.encode()).decode()
            else:
                encode = base64.b64encode(palabra[0].encode()).decode()
            
            guardar_input(encode, archivo="guardado.txt")
            for i in p:
                guardar_input(i,archivo = "guardado.txt")
            for i in pos_pistas:
                guardar_input(str(i), archivo = "pos.txt")
            print("Se guardo el progreso")
            sys.exit()
        elif tecla == "\x1a":  # CTRL + Z
            print(f"        Intentos restantes: {intentos_restantes}")
        elif tecla == "\b":  # BACKSPACE
            if len(texto) > 0:
                texto = texto[:-1]
                print("\b \b", end="", flush=True)

        elif len(texto) < max_len and tecla.isalpha():
            texto += tecla
            print(tecla, end="", flush=True)
    
    return texto

def dar_pista(letras):
    global n_pistas
    global pos_pistas
    x = True
    plo = 0
    if sys.argv[1] == "continuar":
        clave = pal
    else:
        clave = palabra[0]
    if n_pistas == 0:
        print("        Ya no tienes pistas")
    else:
        while(x):
            plo += 1
            letra = random.randint(1,letras)
            if letra not in pos_pistas:
                pos_pistas.append(letra)
                x = False
            if plo > letras:
                x = False
        print(f"        Pista: posicion {letra} tiene {clave[letra-1]}")
        p.append(f"?posicion {letra} tiene {clave[letra-1]}")

def palabra_aleatoria_lista(archivo=documento):
    seleccion = None
    
    with open(archivo, "r", encoding="utf-8") as f:
        for i, linea in enumerate(f, 1):
            linea = linea.strip()
            if not linea:
                continue
            
            if random.randrange(i) == 0:
                seleccion = linea
    
    if seleccion is None:
        return []
    
    return seleccion.split()
if (ACTUALIZAR_LISTA):
    with open(entrada, "r", encoding="utf-8") as f_in, open(salida, "w", encoding="utf-8") as f_out:
        
        for linea in f_in:
            linea = linea.strip()
            
            if "," in linea:
                partes = linea.split(",")
                
                for palabra in partes:
                    f_out.write(palabra.strip() + "\n")
            else:
                f_out.write(linea + "\n")
    # cargar lista de palabras




def existe(palabra, archivo=documento):
    palabra = palabra.lower().strip()

    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            if linea.strip().lower() == palabra:
                return True

    return False

def expansion(palabra):
    lista = {}
    n = 0
    for i in palabra:
        n += 1
        try:
            lista[i].append(n)
        except KeyError:
            lista[i] = [n]
        
        
        
    return lista, n
def menor(a, b):
    if a < b:
        return a
    else:
        return b
def comparar_listas(lista1, lista2):
    comunes = 0
    no_comunes = 0

    limite = min(len(lista1), len(lista2))

    for i in range(limite):
        if lista1[i] == lista2[i]:
            comunes += 1
        else:
            no_comunes += 1

    return comunes, no_comunes
    
def limpiar_archivo(archivo):
    open(archivo, "w").close()
def guardar_input(texto, archivo="palabras_lista.txt"):
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(texto + "\n")
def juego(user, dic, total):
    letras_restantes = {}
    verde = 0
    amarillo = 0
    rojo = 0
     # contar cuántas letras hay en la palabra original
    for letra in dic:
        letras_restantes[letra] = len(dic[letra])

    # contar verdes
    for letra in user:
        if letra in dic:
            for pos in user[letra]:
                if pos in dic[letra]:
                    verde += 1
                    letras_restantes[letra] -= 1

    # contar amarillos
    for letra in user:
        if letra in dic:
            for pos in user[letra]:
                if pos not in dic[letra] and letras_restantes[letra] > 0:
                    amarillo += 1
                    letras_restantes[letra] -= 1

    rojo = total - (verde + amarillo)
    print(f"    verde: {verde}  amarillo: {amarillo}  rojo: {rojo}")
    if verde == total:
        limpiar_archivo("guardado.txt")
        print("Ganaste!")
        print("Intentos: ", intentos)
        try:
            nombre = input("Nombre: ")
        except KeyboardInterrupt:
            sys.exit()
        if sys.argv[1] == "continuar":
            strg = f"{intentos} {nombre} {pal}"
        else:
            strg = f"{intentos} {nombre} {palabra[0]}"
        guardar_input(strg, archivo="Intentos.txt")
        sys.exit()
def main():
    global palabra
    n = 0
    global intentos
    salir = False
    amarillo = 0
    rojo = 0
    verde = 0
    global p
    global pal
    global enable_pistas
    global n_pistas
    global intentos_restantes
    #print(comparar_listas([0,1],[0]))
    try:

        if len(sys.argv) > 1 and sys.argv[1] != "continuar":
            quedate = True
            while quedate:
                palabra = palabra_aleatoria_lista()
                #print("Eligiendo palabra")
                if len(palabra[0]) != int(sys.argv[1]):
                    pass
                else:
                    quedate = False
            dic, total = expansion(palabra[0])
            print(total," letras")
        else:
            if sys.argv[1] != "continuar":
                palabra = palabra_aleatoria_lista()
                print("Eligiendo palabra!")
                
            else:
                nu = 0
                p = []
                if os.path.getsize("guardado.txt") == 0:
                    print("No hay partida guardada")
                    sys.exit()
                with open("guardado.txt", "r",encoding="utf-8") as f:
                    for linea in f:
                        nu += 1
                        if nu == 1:
                            pal = base64.b64decode(linea.strip()).decode()
                            #print(pal)
                        else:
                            
                            p.append(linea.strip())
                with open("pos.txt","r",encoding="utf-8") as f:
                    for linea in f:
                        pos_pistas.append(int(linea))
                pistas = [palabra for palabra in p if palabra.startswith("?")]
                pr = [palabra for palabra in p if not palabra.startswith("?")]
                dic, total = expansion(pal)
                intentos = len(pr)
                n_pistas = n_pistas - len(pistas) 
                print(total," letras")
                if (total <= 3):
                    max_intentos = 5
                elif(total == 4):
                    max_intentos = 10
                elif(total == 5):
                    max_intentos = 20
                elif(total == 6):
                    max_intentos = 25
                elif(total > 6 and total < 9):
                    max_intentos = 20
                elif(total >= 9):
                    max_intentos = 30
                intentos_r = max_intentos - intentos
                if(total >= 7):
                    if (intentos_r <= 5):
                        print("Pistas restantes: ", n_pistas - 1)
                        enable_pistas = True
                print(f"Quedan {intentos_r} intentos")
                for pala in p:
                    if pala.startswith("?"):
                        pala = pala[1:]
                        print("        Pista: ",pala)
                    else:
                        usu, total = expansion(pala)
                        input_limitado(total,auto=pala)
                        juego(usu,dic,total)
    except ValueError:
        print("ERROR")
        sys.exit()
    
    
    #Calcular la cantidad de intentos

    
    
    if sys.argv[1] != "continuar":
            if (total <= 3):
                max_intentos = 5
            elif(total == 4):
                max_intentos = 10
            elif(total == 5):
                max_intentos = 20
            elif(total == 6):
                max_intentos = 25
            elif(total > 6 and total < 9):
                max_intentos = 20
            elif(total >= 9):
                max_intentos = 30
            print(max_intentos," Intentos")
        
    #print(dic, total)
    
    #print(p)
    while not salir:
        
        error = False
        
        u = input_limitado(total).strip().lower()
        intentos_restantes = max_intentos - intentos
        
        
        
        if not existe(u):
            print("         palabra no existe")
            cc = input("        Palabra existe? (y/n)")
            if cc == "y":
                guardar_input(u)
            else:
                error = True
        
        user, t = expansion(u)
        
        #print(user,t)
        if t != total and not error:
            print("largo de palabra incorrecto")
            error = True
        
        if not error:
            p.append(u)
            intentos += 1

            
            juego(user,dic, total)
            if (intentos_restantes == 1):
                print()
                print("Perdiste! Se acabaron los intentos")
                if sys.argv[1] == "continuar":
                    print("La palabra era: ", pal)
                else:
                    print("La palabra era: ", palabra[0])
                sys.exit()
            elif(intentos_restantes <= 4):
                print("        ", intentos_restantes - 1," intentos restantes")
            elif(intentos_restantes == 5):
                if (total >= 7):
                    print("Tienes 3 pistas (Ctrl + A)")
                    enable_pistas = True
            

           

                
                        


        
    

    



if __name__ == "__main__":
    main()
