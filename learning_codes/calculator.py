def main():
    inp = input()
    inp = inp.split()
    x = int(inp[0])
    y = inp[1]
    z = int(inp[2])
    match y:
        case "*":
            print(x*z)
        case "/":
            print(x/z)
        case "-":
            print(x-z)
        case "+":
            print(x+z)
        case "exp":
            print(pow(x,z))

main()
