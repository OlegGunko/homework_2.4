# Задача №1

from pprint import pprint

with open('Recipe.txt', encoding = 'utf - 8') as f:
    # print(f.read())
    cook_book = {}
    for line in f:
        name_dishes = line.strip()
        amount_ingredients = f.readline().strip()
        amount_ingredients = int(amount_ingredients)
        ingredients_list = []
        while amount_ingredients != 0:
            ingredients = f.readline().strip().split('|')
            ingredients_dict = {'ingredient_name': ingredients[0], 'quantity': ingredients[1], 'measure': ingredients[2]}
            amount_ingredients -= 1
            ingredients_list.append(ingredients_dict)
        f.readline().strip()
        cook_book_new = {name_dishes: ingredients_list}
        cook_book.update(cook_book_new)
    # pprint(cook_book)

# Задача №2

    def get_shop_list_by_dishes(dishes, person):
        shop_list_dict = {}
        for name in dishes:
            if name in cook_book.keys():
                for i in cook_book[name]:
                    all_quantity = int(i['quantity'])
                    quantity_per_person = all_quantity * person
                    shop_list_dict_new = {i['ingredient_name']: {'measure': i['measure'], 'quantity': quantity_per_person}}
                    if i['ingredient_name'] in shop_list_dict_new:
                        shop_list_dict_new[i['ingredient_name']]['quantity'] += shop_list_dict_new[i['ingredient_name']]['quantity']
                    shop_list_dict.update(shop_list_dict_new)
        return (shop_list_dict)

    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))