Feature: Create a story

  Scenario: Add Story
    Given I send a basic auth get request "/me"
    And I save the response as "UserInfo1"
    And I set the api token as "UserInfo1.api_token"
    And I send a post request "/projects" with
        |field    |content             |
        |name     |project test python1|
    And I save the response as "project_test"
    And I send a post request to "/stories" with
        |field    |content             |
        |name     |story test|
    Then I verify stories is created with "/stories"