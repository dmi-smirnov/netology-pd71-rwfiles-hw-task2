import os

def read_cook_book(file_path):
    result = dict()
    with open(file_path) as file:
        for line in file:
            dish_name = line.strip()
            result[dish_name] = []
            ingr_amount = int(file.readline().strip())
            for i in range(ingr_amount):
                ingr_info = file.readline().strip().split(' | ')
                result[dish_name].append(
                    {
                        'ingredient_name': ingr_info[0],
                        'quantity': int(ingr_info[1]),
                        'measure': ingr_info[2]
                    }
                )
            file.readline()
    return result

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    result = dict()
    for dish_name in dishes:
        if not dish_name in cook_book.keys():
            print(f'Ошибка: блюдо {dish_name} отсутствует в книге рецепетов.')
            return
        for ingr_dict in cook_book[dish_name]:
            ingr_name = ingr_dict['ingredient_name']
            ingr_quantity = ingr_dict['quantity'] * person_count
            if ingr_name in result.keys():
                result[ingr_name]['quantity'] += ingr_quantity
            else:
                result[ingr_name] = ingr_dict
                result[ingr_name].pop('ingredient_name')
                result[ingr_name]['quantity'] = ingr_quantity
    return result

def main():
    file_name = 'recipes.txt'
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    cook_book = read_cook_book(file_path)

    shop_list = get_shop_list_by_dishes(cook_book,
        ['Запеченный картофель', 'Омлет'], 2)

    print(shop_list)

main()

