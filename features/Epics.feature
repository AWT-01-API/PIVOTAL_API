Feature: Manage Epic
  Background:
    Given I login as user1
    And I create a project with:
    |name|projectEpictest|
  Scenario: Create new Epic
    When I send a put request /projects/{project_id}/epics with:
