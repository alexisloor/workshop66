from behave import given, when, then
from todo_list import ToDoList

# Utilizaremos esta instancia de ToDoListManager en todos los steps
@given('the to-do list is empty')
def step_given_to_do_list_is_empty(context):
    context.manager = ToDoList()

@given('the to-do list contains tasks')
def step_given_to_do_list_contains_tasks(context):
    context.manager = ToDoList()
    for row in context.table:
        context.manager.add_task(row['Task'], row.get('Description', ''))

@then(u'the output should contain')
def step_then_output_should_contain(context):
    for row in context.table:
        task_title = row['Task']
        matching_task = next((task for task in context.manager.tasks if task.title == task_title), None)
        assert matching_task, f'Task "{task_title}" not found in the to-do list.'



@when('the user adds a task "{task_title}"')
def step_when_user_adds_task(context, task_title):
    context.manager.add_task(task_title, '')

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    context.output = context.manager.list_tasks()

@when('the user marks task "{task_title}" as completed')
def step_when_user_marks_task_completed(context, task_title):
    for task in context.manager.tasks:
        if task.title == task_title:
            context.manager.mark_task_completed(task.id)
            break

@when('the user clears the to-do list')
def step_when_user_clears_to_do_list(context):
    context.manager.clear_tasks()

@when('the user edits task "{task_title}" with a new title "{new_title}" and description "{new_description}"')
def step_when_user_edits_task(context, task_title, new_title, new_description):
    for task in context.manager.tasks:
        if task.title == task_title:
            context.manager.edit_task(task.id, new_title, new_description)
            break

@then('the to-do list should contain "{task_title}"')
def step_then_to_do_list_should_contain_task(context, task_title):
    titles = [task.title for task in context.manager.tasks]
    assert task_title in titles, f'Task "{task_title}" not found in the to-do list.'

@then('the output should contain:')
def step_then_output_should_contain_tasks(context):
    for row in context.table:
        task = row['Task']
        assert any(task in t.title for t in context.manager.tasks), f'Task "{task}" not found in the output.'

@then('the to-do list should show task "{task_title}" as completed')
def step_then_to_do_list_should_show_task_completed(context, task_title):
    for task in context.manager.tasks:
        if task.title == task_title:
            assert task.completed, f'Task "{task_title}" is not marked as completed.'
            break

@then('the to-do list should be empty')
def step_then_to_do_list_should_be_empty(context):
    assert len(context.manager.tasks) == 0, 'The to-do list is not empty.'

@then(u'the to-do list should show')
def step_then_to_do_list_should_show(context):
    for row in context.table:
        task_title = row['Task']
        description = row['Description']
        matching_task = next((task for task in context.manager.tasks if task.title == task_title), None)
        assert matching_task, f'Task "{task_title}" not found in the to-do list.'
        assert matching_task.description == description, (
            f'Description for "{task_title}" does not match. '
            f'Expected: "{description}", but got: "{matching_task.description}".'
        )


@then('the to-do list should show:')
def step_then_to_do_list_should_show(context):
    for row in context.table:
        task_title = row['Task']
        description = row['Description']
        matching_task = next((task for task in context.manager.tasks if task.title == task_title), None)
        assert matching_task, f'Task "{task_title}" not found in the to-do list.'
        assert matching_task.description == description, f'Task "{task_title}" description does not match.'
