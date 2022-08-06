from functions import get_drinks_from_ingredients

def mock_drinks_api():
    """
    Returns a list of drinks from the database.
    """
    return [
        {
            'name': 'Coffee',
            'ingredients': ['coffee', 'milk']
        },
        {
            'name': 'Tea',
            'ingredients': ['tea', 'milk']
        },
        {
            'name': 'Cappuccino',
            'ingredients': ['coffee', 'milk', 'sugar']
        }
    ]


def test_get_drinks_from_ingredients():

    available_ingredients = ['coffee', 'milk', 'sugar']
    drinks_database = mock_drinks_api()

    drinks = get_drinks_from_ingredients(available_ingredients, drinks_database)

    assert drinks == ['Coffee', 'Cappuccino']