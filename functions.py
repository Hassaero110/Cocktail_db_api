from api_call_functions import (
    get_all_drinks_containing_ingredient,
    get_cocktail_from_drink_id,
)


def get_drinks_from_ingredients(available_ingredients, drinks_database):
    """
    Returns a list of drinks that can be made from the given ingredients
    """
    list_of_drinks = []

    print("Searching for drinks that only need any of "+ str(available_ingredients))

    for drink in drinks_database:
        can_make_drink = True
        for ingredient in drink["ingredients"]:
            if ingredient not in available_ingredients:
                can_make_drink = False
        if can_make_drink:
            list_of_drinks.append(drink)
    return list_of_drinks

def print_drinks_from_ingredients(available_ingredients, drinks_database, extra_info=False):
            """
            Prints out all drinks that can be made with `available ingredients`
            """

            list_drinks = get_drinks_from_ingredients(available_ingredients, drinks_database)
            print("The cocktails you can make are: ", "\n")
            if list_drinks:
                for drink in list_drinks:

                    if extra_info:
                        print("Cocktail name: " + drink["name"], "\n")
                        print("Ingredients:", "\n")
                        for i in range(len(drink["ingredients"])) :
                            print(str(i+1) + ") " + drink["ingredients"][0],"\n")
                        print("Instructions:","\n")
                        print(drink["instructions"], "\n")
                    else:
                        print(drink["name"], "\n")
            else:
                print("Unfortunately, you can't make any cocktails with these ingredients :(")
                

def get_possible_drinks(available_ingredients):
    """
    Gets a list of drinks which contain any of the available ingredients.
    """
    possible_drinks = []
    
    print("Searching for any drinks containing any of " + str(available_ingredients))
    for available_ingredient in available_ingredients:
        possible_drinks += get_all_drinks_containing_ingredient(available_ingredient)

    return set(possible_drinks)


def create_drinks_database(drinks_list):
    """
    Returns a list of drinks with name, ingredients and
    instructions for each drink as a dictionary
    """

    drinks_database = []

    for drink in drinks_list:
        details = get_cocktail_from_drink_id(drink)

        drinks_database.append({
            "name": details["name"], 
            "instructions": details["instructions"], 
            "ingredients": details["ingredients"]
        })

    return drinks_database
