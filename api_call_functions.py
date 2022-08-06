import json
from urllib.error import HTTPError

import requests


def get_all_drinks_containing_ingredient(available_ingredient):
    """
    Get a list of drink ids which contain `available_ingredient`
    """
    available_ingredient = available_ingredient.replace(" ", "%20")

    url = r"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i="
    url_query = url + available_ingredient
    response = requests.get(url_query)

    drinks = []

    if response.status_code == 200:
        if response.text is not None:
            tt = json.loads(response.text)

            for drink in tt["drinks"]:
                drinks.append(drink["idDrink"])
    else:
        raise HTTPError("Failed to get response: " + response.status_code)

    return drinks


def get_all_ingredients_from_drink_id(drink_id):
    """
    Get a list of ingredients for a `drink id`
    """
    url = r"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i="
    url_query = url + str(drink_id)

    response = requests.get(url_query)

    tt = json.loads(response.text)
    ingredients = []

    if response.status_code == 200:
        if tt["drinks"] is not None:
            if len(tt["drinks"]) > 0:
                for k, v in tt["drinks"][0].items():
                    if "strIngredient" in k and v is not None:
                        ingredients.append(v)
                        # if api guaranteed null ingredients come last then could
                        # break to speed up
    else:
        raise HTTPError("Failed to get response: " + response.status_code)

    return ingredients
