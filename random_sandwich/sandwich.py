from random import choice, seed
from functools import reduce
import operator
import numpy as np
import json


def choose_ingredient_from_file(path: str):
    with open(path, 'r', encoding='utf-8-sig') as f:
        ingredients = json.load(f)
        return choice(ingredients)


def bread_advice(bread):
    advice = choose_ingredient_from_file('ingredients/bread_advice.json')
    return '(' + advice['Advice'] + ' ' + bread['Name'] + '!)'


def get_bread():
    return choose_ingredient_from_file('ingredients/bread.json')


def get_meat():
    return choose_ingredient_from_file('ingredients/meat.json')


def get_seafood():
    return choose_ingredient_from_file('ingredients/seafood.json')


def get_dairy():
    return choose_ingredient_from_file('ingredients/dairy.json')


def get_veg():
    return choose_ingredient_from_file('ingredients/veg.json')


def get_sauce():
    return choose_ingredient_from_file('ingredients/sauce.json')


def get_extras():
    return choose_ingredient_from_file('ingredients/extras.json')


def get_non_filling():
    return choose_ingredient_from_file('ingredients/nonfilling.json')


def get_random_intro():
    return choice(['Sotd.', 'Sotd:', 'Sotd', 'SOTD', 'SOTD:', 'SOTD.'])


def no_ingredient():
    return {'Name': '', 'PriceInPence': 0}


def ingredient_chosen(ingredient):
    return ingredient['Name'] != ''


def total_price(bread, ingredients):
    return int(bread['PriceInPence']) + reduce(
        operator.add, map(lambda i: int(i['PriceInPence']), ingredients), 0
    )


def build_description(ingredients):
    return ', '.join(map(lambda i: i['Name'], ingredients))


def make_sandwich(random_seed):
    seed(random_seed)
    np.random.seed(random_seed)

    bread = get_bread()

    main_filling_choices = [
        get_meat(),
        get_seafood(),
        get_non_filling(),
        no_ingredient(),
    ]
    main_filling = main_filling_choices[
        np.random.choice(len(main_filling_choices), p=[0.53, 0.37, 0.06, 0.04])
    ]

    veg1 = get_veg()

    optional_veg2 = [no_ingredient(), get_veg()]
    veg2 = optional_veg2[np.random.choice(len(optional_veg2), p=[0.8, 0.2])]

    optional_dairy = [get_dairy(), no_ingredient()]
    dairy = optional_dairy[np.random.choice(len(optional_dairy), p=[0.7, 0.3])]

    sauce = get_sauce()

    optional_extras = [get_extras(), no_ingredient()]
    extras = optional_extras[
        np.random.choice(len(optional_extras), p=[0.15, 0.85])
    ]

    ingredients = []

    if ingredient_chosen(main_filling):
        ingredients.append(main_filling)

    if ingredient_chosen(dairy):
        ingredients.append(dairy)

    ingredients.append(veg1)

    if ingredient_chosen(veg2):
        ingredients.append(veg2)

    ingredients.append(sauce)

    if ingredient_chosen(extras):
        ingredients.append(extras)

    text = ' '.join(
        [
            get_random_intro(),
            build_description(ingredients),
            bread_advice(bread),
        ]
    )

    # text += ', £{0:.2f}'.format(priceInPence / 100.0)

    return text, total_price(bread, ingredients)
