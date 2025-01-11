import pytest
from pytest_bdd import scenario,scenarios,given,when,then
from pathlib import Path

featureFileDir='features'
featureFile='firstFeature.feature'
BASE_DIR=Path(__file__).resolve().parent.parent
FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

def pytest_configure():
    pytest.AMT=0

scenarios(FEATURE_FILE)
# if we want to run using feature files then use 'scenarios' (line # 13)
# then run comment the below line from 15-18 and 33-35, before running it.
# if we want to run a specific feature then comment line #13 and uncomment lines 15-18 and 33-35

# @scenario(FEATURE_FILE,'Withdrawal of money')
# def test_withdrawal():
#     print("End of Withdrawal test")
#     pass

@given("the account balance is 100")
def current_balance():
    pytest.AMT=100

@when("the account holder withdraws 30")
def withdraw_amount():
    pytest.AMT=pytest.AMT-30

@then("the account balance should be 70")
def final_balance():
    print("Final Balance is => ",pytest.AMT)
    assert pytest.AMT==70

# @scenario(FEATURE_FILE,'Removal of data from a set')
# def test_removal_of_items():
#     pass

# Pytest_BDD_Notes - target_fixture a special parameter can be used in the same test scenarios.
# target_fixture are available for other given,when,then step definition functions in the same test scenarios
@given('A set of 3 fruits',target_fixture='my_set')
def current_balance():
    fruit_set={"apple","banana","cherry"}
    return fruit_set

@when('We remove a fruit from set')
def remove_fruit(my_set):
    my_set.pop()
    print(my_set)

@then('the set will have 2 fruits')
def final_fruits(my_set):
    assert len(my_set)==2