Feature: Manage Epic
  Background:
    Given I login as "user1"
  Scenario: Create new Epic
    When I create a project with
        |field    |content     |
        |name     |project test1|
    And I save the response as "projectEpics"
    And I create a epic with
        |field|content      |
        |name |epic test  asd|
    And I save the response as "Epic1"
    Then I verify epic is created
    And I verify epic body is correct
