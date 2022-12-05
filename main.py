import os

filename = 'recipes.txt'

cook_book = dict()

path = os.path.join(os.path.dirname(__file__), filename)
with open(path) as file:
    for line in file:
        dish_name = line.strip()
        cook_book[dish_name] = []
        ingr_amount = int(file.readline().strip())
        for i in range(ingr_amount):
            ingr_info = file.readline().strip().split(' | ')
            cook_book[dish_name].append(
                {
                    'ingredient_name': ingr_info[0],
                    'quantity': ingr_info[1],
                    'measure': ingr_info[2]
                }
            )
        file.readline()

print(cook_book)

