from pytest_bdd import scenario,scenarios,given,when,then,parsers
import pytest
from pathlib import Path

featureFileDir='features'
featureFile='dataTables.feature'
BASE_DIR=Path(__file__).resolve().parent.parent
FEATURE_FILE=BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

scenarios(FEATURE_FILE)

@given('print the given statement')
def print_statement():
    print("Printing the Given scenario")

@when('following data are available')
def data_available(datatable):
    for r in datatable[1:]:
        print(r)
        print(type(r))

@then('print the details')
def print_details():
    print('printing the details')

@when('print the below data')
def print_details(datatable):
    print('---------',datatable)
    for r in datatable:
        print(r)
