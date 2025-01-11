Feature: Fixture and BDD Backgroung on the Python Set DataType
  Background:
    Given A data type is set
    And The set is not empty

  Scenario: Adding to a set
    Given A set with 3 elements
    When Add 2 elements to the set
    Then The set should have 5 elements