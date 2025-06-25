def main():
    camel = input("camelCase: ")
    out = False
    while True:
        if camel[0].isupper():
            print("error en formato: primera letra no es minuscula")
            out = True
            break
        for i in range(len(camel)):
            if camel[i].isspace():
                print("error en formato: No tiene que haber espacios")
                out = True
                break 
        break
            

    #fuera del loop
    if not out:
        nueva = ""
        for i in camel:
            if i.isupper():
                nueva += "_" + i.lower()
            else:
                nueva += i
        print(f"snake_case: {nueva}")

main()