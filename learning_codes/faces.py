
def main():
    n = input("Introduzca una carita: ")
    convert(n)

def convert(inp):
    inp = inp.replace(':(', "\u2639").replace(":)", "\u263a")
    print(inp)
    
main()