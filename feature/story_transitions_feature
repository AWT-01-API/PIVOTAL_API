Feature: story transition api request

  Background:
    Given I send a basic auth get request "/me"
    And I save the response as "UserInfo1"
    And I set the api token as "UserInfo1.api_token"
    And I send a post request "/projects" with
        |name | project test        |
    And I save the response as "Project1"
    And I send a post request "/projects/{Project1.id}/stories" with
        |name | story test          |
    And I save the response as "Story1"
    And I send a put request "/projects/{Project1.id}/stories/{Story1.id}" with
        |current_state | started    |
        |estimate      | 1          |
    And I save the response as "Story1-Update1"
    And I send a put request "/projects/{Project1.id}/stories/{Story1.id}" with
        |current_state | finished   |
    And I save the response as "Story1-Update2"
    And I send a put request "/projects/{Project1.id}/stories/{Story1.id}" with
        |current_state | delivered  |
    And I save the response as "Story1-Update3"
    And I send a put request "/projects/{Project1.id}/stories/{Story1.id}" with
        |current_state | rejected   |
    And I save the response as "Story1-Update4"
    And I send a put request "/projects/{Project1.id}/stories/{Story1.id}" with
        |current_state | accepted   |
    And I save the response as "Story1-Update5"

  Scenario: request story transitions
    And I send a get request "/projects/{project_id}/story_transitions"
    And I save the response as "StoryTransitions1"
    Then I verify response "StoryTransition1" is equal to
        "[
          {
               "kind": "story_transition",
               "state": "unscheduled",
               "story_id": {Story1.id},
               "project_id": {Project1.id},
               "project_version": 2,
               "occurred_at": {Story1.updated_at},
               "performed_by_id": {UserInfo1.id}
          },
          {
               "kind": "story_transition",
               "state": "started",
               "story_id": {Story1.id},
               "project_id": {Project1.id},
               "project_version": 3,
               "occurred_at": {Story1-Update1.updated_at},
               "performed_by_id": {UserInfo1.id}
          },
          {
               "kind": "story_transition",
               "state": "finished",
               "story_id": {Story1.id},
               "project_id": {Project1.id},
               "project_version": 3,
               "occurred_at": {Story1-Update2.updated_at},
               "performed_by_id": {UserInfo1.id}
          },
          {
               "kind": "story_transition",
               "state": "delivered",
               "story_id": {Story1.id},
               "project_id": {Project1.id},
               "project_version": 3,
               "occurred_at": {Story1-Update3.updated_at},
               "performed_by_id": {UserInfo1.id}
          },
          {
               "kind": "story_transition",
               "state": "rejected",
               "story_id": {Story1.id},
               "project_id": {Project1.id},
               "project_version": 3,
               "occurred_at": {Story1-Update4.updated_at},
               "performed_by_id": {UserInfo1.id}
          },
          {
               "kind": "story_transition",
               "state": "accepted",
               "story_id": {Story1.id},
               "project_id": {Project1.id},
               "project_version": 3,
               "occurred_at": {Story1-Update5.updated_at},
               "performed_by_id": {User1.id}
          },
         ]
        "