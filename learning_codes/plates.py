def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    n1 = False
    for i in s:
        #Verficia que el primer numero no sea 0
        if i.isdigit():
            if not n1:
                if i == "0":
                    return False
                n1 = True
        else:
            if n1:
                return False
    return True
main()