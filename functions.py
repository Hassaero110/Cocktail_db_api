from api_call_functions import (
    get_all_drinks_containing_ingredient,
    get_all_ingredients_from_drink_id,
)


def get_drinks_from_ingredients(available_ingredients, drinks_database):
    """
    Returns a list of drinks that can be made from the given ingredients.
    """
    drinks = []

    for drink in drinks_database:

        can_make_drink = True
        for ingredient in drink["ingredients"]:
            if ingredient not in available_ingredients:
                can_make_drink = False
        if can_make_drink:
            drinks.append(drink["name"])

    return drinks


def get_possible_drinks(available_ingredients):
    """
    Gets a list of drinks which contain any of the available ingredients.
    """
    possible_drinks = []

    for available_ingredient in available_ingredients:
        print("Searching for drinks containing: " + available_ingredient)
        possible_drinks += get_all_drinks_containing_ingredient(available_ingredient)

    return set(possible_drinks)


def create_drinks_database(drinks_list):

    drinks_database = []

    for drink in drinks_list:
        ingredients = get_all_ingredients_from_drink_id(drink)

        drinks_database.append({"name": drink, "ingredients": ingredients})

    return drinks_database
