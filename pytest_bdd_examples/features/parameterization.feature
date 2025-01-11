@bdd_parameterized
Feature: Parameterizing tests in Pytest BDD
  Scenario: check varieties of fruit
    Given there are 3 varieties of fruits
    When we add a same variety of fruit
    Then there is same count of varieties
    But if we add a different variety of fruit
    Then the count of varieties increases to 4

  @eat_fruits
  Scenario: Parameterize benefits
    Given there are 5 fruits
    When i eat 3 fruits
    And i eat 2 fruits
    Then i should have 0 fruits