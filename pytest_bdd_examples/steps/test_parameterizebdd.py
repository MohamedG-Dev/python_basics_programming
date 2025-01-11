from pytest_bdd import scenario,scenarios,given,when,then,parsers
import pytest
from pathlib import Path

featureFileDir='features'
featureFile='parameterization.feature'
BASE_DIR=Path(__file__).resolve().parent.parent
FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

scenarios(FEATURE_FILE)

@given('there are 3 varieties of fruits',target_fixture='fruits_set')
def existing_fruits():
    fruits={'apple','banana','mango'}
    return fruits

@when('we add a same variety of fruit')
def add_fruit(fruits_set):
    fruits_set.add('apple')

@then('there is same count of varieties')
def same_count(fruits_set):
    assert len(fruits_set)==3

@then('if we add a different variety of fruit')
def add_different_fruit(fruits_set):
    fruits_set.add('guava')

# Applying parameterization below:
# for int/numbers we need provide d. d means digit
@then(parsers.parse('the count of varieties increases to {count:d}'))
def count_increases(fruits_set,count):
    print(fruits_set)
    assert len(fruits_set)==count

# # # # # # # # END OF FIRST SCENARIO # # # # # # # # # # #
# # # # # # # # START OF SECOND SCENARIO # # # # # # # # # # #
# Global variable declaration in pytest
pytest.total_fruits=0
@given(parsers.parse('there are {count:d} fruits'),target_fixture='start_fruits')
def existing_fruits(count):
    pytest.total_fruits=count
    return dict(start=count,eat=0)

# for both the statements, same method will be executed
# When i eat 3 fruits
# And i eat 2 fruits
@when(parsers.parse('i eat {eat:d} fruits'))
def eat_fruits(start_fruits,eat):
    start_fruits["eat"] +=eat
    print('The fruits eaten are:',start_fruits)

@then(parsers.parse('i should have {left:d} fruits'))
def should_have_left_fruits(start_fruits,left):
    assert start_fruits['start'] == pytest.total_fruits
    assert pytest.total_fruits - start_fruits['eat'] == left