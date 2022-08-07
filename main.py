import sys

from functions import (
    create_drinks_database,
    get_possible_drinks,
    print_drinks_from_ingredients,
)

if __name__ == "__main__":

    # Turn comma separated values into a list of ingredients
    ingredients = ""
    if len(sys.argv) > 1:  
        for count, arg in enumerate(sys.argv[1:]):
            ingredients += arg + " "
    else:
        print("No ingredients provided")
        sys.exit()
    ingredients = ingredients.split(",")
    available_ingredients = [ingredient.strip() for ingredient in ingredients]

    # Get all drinks which contain any of the available ingredients
    possible_drinks = get_possible_drinks(available_ingredients)

    # Get all ingredients for all drinks in possible_drinks
    drinks_database = create_drinks_database(possible_drinks)

    # Get all drinks that can be made from the available ingredients
    print_drinks_from_ingredients(available_ingredients, drinks_database, True)


