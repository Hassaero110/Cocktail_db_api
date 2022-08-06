import pytest
from functions import get_drinks_from_ingredients, get_possible_drinks


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


@pytest.mark.parametrize(
    "test_ingredients,expected", 
    [([],[]), # return empty list for empty ingredients
    (['chorizo'], []), # return empty list for ridiculous ingredients
    (['coffee', 'milk'], ['Coffee']), # Can only make coffee with coffee and milk
    (['coffee', 'milk', 'chorizo'], ['Coffee']), # Extra ingredients don't affect results unless drink is available
    (['coffee', 'milk', 'tea'], ['Coffee', 'Tea']), # Can make coffee and tea
    (['coffee', 'milk', 'tea', 'sugar'], ['Coffee', 'Tea', 'Cappuccino']) # can make all test drinks
    ]
    )
def test_get_drinks_from_ingredients(test_ingredients, expected):

    drinks_database = mock_drinks_api()

    drinks = get_drinks_from_ingredients(test_ingredients, drinks_database)

    assert sorted(drinks) == sorted(expected)

@pytest.fixture
def mock_get_all_drinks_containing_ingredient(monkeypatch):

    def mock_get_all_drinks_containing_ingredient_func(available_ingredient):
        """
        Use mock drinks api to get drinks
        """
        all_drinks = mock_drinks_api()
        drinks_list = [ 
            drink['name'] for drink in all_drinks if available_ingredient in drink['ingredients'] 
        ]
        return drinks_list

    monkeypatch.setattr(
        'functions.get_all_drinks_containing_ingredient',
        mock_get_all_drinks_containing_ingredient_func,
    )


@pytest.mark.parametrize(
    "test_ingredients,expected", 
    [([],[]), # return empty list for empty ingredients
    (['sugar'], ['Cappuccino']), # Cappuccino is the only drink which has sugar
    (['sugar', 'tea'], ['Cappuccino', 'Tea']) # Cappuccino and Tea only drinks which contain one of these ingredients
    ]
    )
def test_get_all_drinks_containing_ingredient(mock_get_all_drinks_containing_ingredient,test_ingredients,expected ):
    """
    Get a list of drinks which contain `available_ingredient`
    """
    drinks = get_possible_drinks(test_ingredients)

    assert sorted(drinks) == sorted(expected)