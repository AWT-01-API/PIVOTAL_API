Feature: Create new Project

  Scenario: scenario project
    When I send a post request "/projects" with
        |field    |content             |
        |name     |project test python2|

