from pytest_bdd import scenario,scenarios,given,when,then
from pathlib import Path
import pytest

featureFileDir='features'
featureFile='fixtures.feature'
BASE_DIR=Path(__file__).resolve().parent.parent
FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

scenarios(FEATURE_FILE)

@pytest.fixture()#default scope
def setup_set():
    print("\n In fixture... setup() function.. \n ")
    countries={'Poland','Iceland','Ireland','Germany','France'}
    # uncomment the below line # to fail a test case
    # countries={}
    # uncomment the below line to fail the test case at background level - given
    # countries=[]
    # uncomment the below line to fail the test case at background level - Given(And)
    # countries =set()
    return countries

@given('A data type is set')
def check_set_type(setup_set):
    print("executing background steps to check set type")
    if not isinstance(setup_set,set):
        pytest.xfail("the type is not set")

@given('The set is not empty')
def check_set_not_empty(setup_set):
    print('Inside Background checking non-empty set')
    if len(setup_set)==0:
        pytest.xfail("the set is empty")

@given('A set with 3 elements',target_fixture='countries_set')
def set_of_elements(setup_set):
    if len(setup_set)==0:
        pytest.xfail("The set of elements is empty")
    elif len(setup_set) > 3:
        while len(setup_set) > 3:
            setup_set.pop()
    return setup_set

@when('Add 2 elements to the set')
def add_elements(countries_set):
    countries_set.add('Italy')
    countries_set.add('Turkey')

@then('The set should have 5 elements')
def final_set_elements(countries_set):
    print("Countries are: ",countries_set)
    assert len(countries_set)==5