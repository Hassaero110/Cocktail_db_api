import sys

from functions import (
    create_drinks_database,
    get_drinks_from_ingredients,
    get_possible_drinks,
)

if __name__ == "__main__":

    # Turn comma separated values into a list of ingredients
    ingredients = ""
    for count, arg in enumerate(sys.argv[1:]):
        if count < len(sys.argv[1:]) - 1 and "," not in arg:
            ingredients += arg + " "
        else:
            ingredients += arg

    available_ingredients = ingredients.split(",")

    # Get all drinks which contain any of the available ingredients
    possible_drinks = get_possible_drinks(available_ingredients)

    # Get all ingredients for all drinks in possible_drinks
    drinks_database = create_drinks_database(possible_drinks)

    # Get all drinks that can be made from the available ingredients
    allowed_drinks = get_drinks_from_ingredients(available_ingredients, drinks_database)

    # Print the allowed drinks
    print(allowed_drinks)
