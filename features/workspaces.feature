Feature: New Workspace

  @deleteWorkspace
  Scenario: Create a new workspace
    Given I login as "user1"
    And I send a post request "/workspaces" with
      | name | test |
    And I save the response as "Workspace1"
    Then I verify if the workspace is created with "Workspace1" data