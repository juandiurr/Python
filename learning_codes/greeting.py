greeting = input("Salutate: ")

def main(): 
    res = find()   
    if res == 1:
        print("$0")
    elif res == 2:
        print("$20")
    else:
        print("$100")

def find():
    if "h" in greeting.lower():
        if "hello" in greeting.lower():
            return 1
        else:
            return 2
    else:
        return 3

main()