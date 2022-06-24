from random import choice, seed
import numpy as np
import json


def choose_ingredient_from_file(path: str):
    with open(path) as f:
        ingredients = json.load(f)
        return choice(ingredients)


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


def make_sandwich(random_seed):
    seed(random_seed)

    main_filling_choices = [
        get_meat(),
        get_seafood(),
        get_non_filling(),
        ('', 0),
    ]
    main_filling = main_filling_choices[
        np.random.choice(len(main_filling_choices), p=[0.53, 0.37, 0.06, 0.04])
    ]

    veg1 = get_veg()

    optional_veg2 = [('', 0), get_veg()]
    veg2 = optional_veg2[np.random.choice(len(optional_veg2), p=[0.8, 0.2])]

    optional_dairy = [get_dairy(), ('', 0)]
    dairy = optional_dairy[np.random.choice(len(optional_dairy), p=[0.7, 0.3])]

    sauce = get_sauce()

    optional_extras = [get_extras(), ('', 0)]
    extras = optional_extras[
        np.random.choice(len(optional_extras), p=[0.15, 0.85])
    ]

    text = 'S.O.T.D '

    if main_filling[0] != '':
        text += main_filling[0] + ', '
    if dairy[0] != '':
        text += dairy[0] + ', '
    text += veg1[0] + ', '
    if veg2[0] != '':
        text += veg2[0] + ', '
    text += sauce[0]
    if extras[0] != '':
        text += ', ' + extras[0]

    price = (
        200
        + main_filling[1]
        + veg1[1]
        + veg2[1]
        + dairy[1]
        + sauce[1]
        + extras[1]
    )

    text += ', £{0:.2f}'.format(price / 100)

    return text
