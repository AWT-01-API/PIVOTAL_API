Feature: Manage Epic
  Scenario: Create new Epic
    Given I send a basic auth get request "/me"
    And I save the response as "UserInfo1"
    And I set the api token as "UserInfo1.api_token"
    And I send a post request "/projects" with
        |field    |content             |
        |name     |project test pythonvl2|
    And I save the response as "projectEpics"
    And I send a post request epic "/projects/{project_id}/epics" with
        |field|content      |
        |name |epic test  asd|
    Then I verify epic is created
    Then I verify epic body is correct