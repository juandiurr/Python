from encrypter import Psswrd, decrypt
from sys import exit
import csv
import os
def main():
    if not os.path.isfile("archivo.txt"):
        starter_pass = Psswrd("hashed")
        with open("archivo.txt", "x", encoding="utf-8") as archivo:
            hash = starter_pass.encrypt(input("Introduzca contraseña para ingresar a aplicación: "))
            archivo.write(hash)
        print("✅ Contraseña guardada.")
    else:
        with open("archivo.txt", "r", encoding="utf-8") as archivo:

            starter = Psswrd(archivo.read())

        for intentos_restantes in range(3, 0, -1):
            token = input(f"🔑 Introduzca contraseña (Intentos restantes: {intentos_restantes}): ")
            if starter.verify(token):
                print("✅ Acceso concedido.")
                break
            else:
                print("❌ Contraseña incorrecta.")
        else:
            print("🚫 Acceso denegado. Demasiados intentos fallidos.")
            exit()


            

    while True:
        
        print("1. Registrar contraseña")
        print("2. Verficiar contraseña")
        
            
        try:
            i = input()
        except KeyboardInterrupt:
            exit()

        if i == "1":
            registrar()
        elif i == "2":
            verificar()
            
    """datos = [
    {"nombre": "Ana", "edad": 21},
    {"nombre": "Luis", "edad": 25}
]"""

def registrar():
    rr = Psswrd("crypt")

    red = rr.encrypt(input("Red: ").strip()).decode()
    red_c = rr.clave.decode()
    con = Psswrd("crypt")
    contra = con.encrypt(input("Contraseña: ").strip()).decode()
    fer = con.clave.decode()
    existe = os.path.isfile("datos.csv")
    with open("datos.csv", "a", newline='', encoding='utf-8') as archivo:
        campos = ["ooo", "ooi","oio","ioo"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        if not existe or os.stat("datos.csv").st_size == 0:
            escritor.writeheader()
        escritor.writerow({"ooo": red, "ooi": contra, "oio": fer, "ioo":red_c})
    print("Contraseña registrada exitosamente.")
def verificar():
    with open('datos.csv', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(decrypt(fila["ooo"], fila["ioo"]), end=' ')
            print(decrypt(fila["ooi"], fila["oio"]))
        
                    


    
if __name__ == "__main__":
    main()