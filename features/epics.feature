Feature: Manage Epic
  Scenario: Create new Epic
      Given I send a basic auth get request "/me"
    And I save the response as "UserInfo1"
    And I set the api token as "UserInfo1.api_token"
    And I send a post request "/projects" with
        |field    |content             |
        |name     |project test python2|
    And I save the response as "projectEpics"
    Then I verify the status code is 200


    When I get the response of the past project
    #When I send a post request "/projects/2202474/epics" with
    #    |field|content      |
    #    |name |epic test  asd|
