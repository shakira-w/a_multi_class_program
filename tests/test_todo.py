from lib.todo import Todo

def test_add_todo_returns_task_and_complete():
    todo = Todo("Learn to spell")
    assert todo.task == "Learn to spell"
    assert todo.complete == False

def test_mark_complete():
    todo = Todo("Learn to spell")
    todo.mark_complete()
    assert todo.complete == True