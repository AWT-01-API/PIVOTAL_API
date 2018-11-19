Feature: New Workspace

  Background:
    Given I login as "user3"

  Scenario: Create a new workspace
    When I create a workspace with
      | field | content |
      | name  | Test    |
    And I save the response as "workspace1"
    Then I verify if the response status code is "200"
    Then I verify if the response body is from a "workspace"
    Then I verify if "workspace1" is created

