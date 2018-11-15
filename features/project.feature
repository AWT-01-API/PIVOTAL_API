Feature: Create new Project
  Scenario: project
    Given I login as "user1"
    And I create a "/projects" with data:
    Given a <name>
    |name       |
    |testproject|
    And I verify the status code is "200"

