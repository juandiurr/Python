def main():
    lista = {}
    while True:
        try:
            i = input()
        except KeyboardInterrupt:
            for o in lista:
                print(f"{o}: {lista[o]}")
            break
        else:
            if i not in lista:
                lista[i] = 1
            else:
                lista[i] = 1 + lista[i]
main()