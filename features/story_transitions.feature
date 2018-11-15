Feature: story transition api request

  Scenario: scenario project
    Given I send a basic auth get request "/me"
    And I save the response as "UserInfo1"
    And I set the api token as "UserInfo1.api_token"
    And I send a post request "/projects" with
        |field    |content             |
        |name     |project test python2|