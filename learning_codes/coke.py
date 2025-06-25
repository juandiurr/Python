def main():
    print("Amount due: 50")
    due = 50
    coint = 0
    out = False
    while due > 0:
        coin = int(input("Insert coin: "))
        coint += coin
        if coin != 25 and coin != 10 and coin != 5:
            out = True
            break
        else:
            due = due - coin
            print(f"Amount due: {due}")
            
    if not out:
        print(f"Change: {coint - 50}")
    else: 
        print(f"Invalide coin: {coint}")
main()