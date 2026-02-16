from lib.todo_list import TodoList
from lib.todo import Todo

"""
if we add todos to the todo list, we should get a list with the todos

"""
def test_add_todos_returns_list_of_todos():
    todo_list = TodoList()
    todo_1 = Todo("Clean my room")
    todo_2 = Todo("Do laundry")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    result = todo_list.display_list()
    assert result == [todo_1, todo_2]

def test_incomplete_returns_list_of_incomplete_todos():
    todo_list = TodoList()
    todo_1 = Todo("Clean my room")
    todo_2 = Todo("Do laundry")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_1.mark_complete()
    result = todo_list.incomplete()
    assert result == [todo_2]

def test_complete_returns_list_of_complete_todos():
    todo_list = TodoList()
    todo_1 = Todo("Clean my room")
    todo_2 = Todo("Do laundry")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_1.mark_complete()
    result = todo_list.complete()
    assert result == [todo_1]

def test_give_up_marks_todos_as_complete():
    todo_list = TodoList()
    todo_1 = Todo("Clean my room")
    todo_2 = Todo("Do laundry")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.give_up()
    assert todo_list.complete() == [todo_1, todo_2]
    assert todo_list.incomplete() == []