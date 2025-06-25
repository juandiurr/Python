import sys

def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except KeyboardInterrupt:
            print("\nAdieu, adiue to ", end = "")
            n = 1
            for i in names:
                if n == len(names):#ultimo nombre
                    print("and", i)
                else:
                    print(i + ",", end = " ")
                n += 1
            sys.exit()





main()