Feature: New Workspace

  Background:
    Given I login as "user1"

  Scenario: Create a new workspace
    When I create a workspace with
      | field | content |
      | name  | Test    |
    And I save the response as "workspace1"
    Then I verify if the response status code is "200"
    Then I verify if the "workspace" body is correct
    Then I verify if "workspace1" is created

  Scenario: Edit a workspace: Add projects
    When I create a project with
      | field | content |
      | name  | Test    |
    And I save the response as "project2"
    And I create a workspace with
      | field | content |
      | name  | Test    |
    And I save the response as "workspace2"
    And I add "project1" to the workspace "workspace2"
    Then I verify if the response status code is "200"
    Then I verify if "project1" exists in "workspace1"

  Scenario: Edit a workspace: Modify name field
    When I create a workspace with
      | field | content |
      | name  | Test    |
    And I save the response as "workspace3"
    And I edit "workspace3" with
      | field | content |
      | name  | newName |
    Then I verify if the response status code is "200"
    Then I verify if the "workspace" body is correct
    Then I verify if the field "name" of "workspace3" is correct

  Scenario: Delete a workspace
    When I create a workspace with
      | field | content |
      | name  | Test    |
    And I save the response as "workspace4"
    And I delete "workspace4"
    Then I verify if the response status code is "200"
    Then I verify if "workspace4" is deleted
