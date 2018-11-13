Feature: Create new Epic
  Background:
    Given I login as "user1"
    And I create a "/project" with data:
    |name            |testproject|
    |new_account_name|testaccount|
    And I verify the status code is "200"
    And I store the response as "Project1"

  @deleteProject
  Scenario: Create an new Epic with title only
    When I open a project "Project1.name"
    And I click the add epics button
    And I fill the epic
    |title|testEpic|
    And I store the table as "Epic1"
    Then I verify id epic title is "Epic1.title"
