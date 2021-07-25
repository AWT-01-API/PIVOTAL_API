Feature: Create new Project

  Background:
    Given I login as "user1"

  Scenario: scenario project
    When I create a project with
      | field | content      |
      | name  | test python2 |
    Then I validate that "test python2" project is created

