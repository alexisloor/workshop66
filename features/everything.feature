Feature: To-Do List Management

Scenario: Add a task to the to-do list
  Given the to-do list is empty
  When the user adds a task "Buy groceries"
  Then the to-do list should contain "Buy groceries"

Scenario: List all tasks in the to-do list
  Given the to-do list contains tasks:
    | Task          |
    | Buy groceries |
    | Pay bills     |
  When the user lists all tasks
  Then the output should contain:
    | Task          |
    | Buy groceries |
    | Pay bills     |

Scenario: Mark a task as completed
  Given the to-do list contains tasks:
    | Task          | Status   |
    | Buy groceries | Pending  |
  When the user marks task "Buy groceries" as completed
  Then the to-do list should show task "Buy groceries" as completed

Scenario: Clear the entire to-do list
  Given the to-do list contains tasks:
    | Task          |
    | Buy groceries |
    | Pay bills     |
  When the user clears the to-do list
  Then the to-do list should be empty

Scenario: Edit a task in the to-do list
  Given the to-do list contains tasks:
    | Task            | Description        |
    | Buy groceries   | Buy milk and eggs  |
  When the user edits task "Buy groceries" with a new title "Buy groceries and cleaning supplies" and description "Buy milk, eggs, and soap"
  Then the to-do list should show:
    | Task                                | Description               |
    | Buy groceries and cleaning supplies | Buy milk, eggs, and soap  |
