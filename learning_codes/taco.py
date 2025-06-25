menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
#x = input("Item: ")
amount = 0
while True:
    try:
        x = input("Item: ")
    except KeyboardInterrupt:
        print(f"\nTotal due: {amount}")
        break

    try:
        amount = amount + menu[x]
    except KeyError:
        pass
    else:
        print(f"total: {amount}")
        