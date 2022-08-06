def get_drinks_from_ingredients(available_ingredients, drinks_database):
    """
    Returns a list of drinks that can be made from the given ingredients.
    """
    drinks = []

    for drink in drinks_database:

        can_make_drink = True
        for ingredient in drink['ingredients']:
            if ingredient not in available_ingredients:
                can_make_drink = False
        if can_make_drink:
            drinks.append(drink['name'])

    return drinks