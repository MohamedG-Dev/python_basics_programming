Feature: scenario outline example

  Scenario Outline: Scenario outline test example
    Given there are <start> cucumbers
    When I deposit <deposit> cucumbers
    And I withdraw <withdraw> cucumbers
    Then I should <final> cucumbers
    Examples:
    |start|deposit|withdraw|final|
    |12   |5      |7       |10   |
    |10   |5      |20      |-5   |
    |10   |5      |20      |-9   |