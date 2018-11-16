Feature: New Workspace

  Scenario: Create a new workspace
    Given I login as "user1"
    And I a workspace with fields:
      | name | test |
    And I save the response as "Workspace1"
    Then I verify if the workspace is created
