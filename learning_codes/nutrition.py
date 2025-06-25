dick = {
    "apple":"130",
    "avocado":"50",
    "banana":"110",
    "cantaloupe":"50",
    "grapefruit":"60",
    "grapes":"90",
    "kiwifruit":"90",
    "lemon":"15",
    "lime":"20",
}
fruit = input("Item: ").lower()
"""
if fruit in dick:
    print(f"Calories: {dick[fruit]}")
else:
    print("Fruit is not in the dictionary")
    """
try:
    print(f"Calories: {dick[fruit]}")
except KeyError:
    print("Fruit is not in the dictionary")