from lib.todo_list import TodoList

def test_initially_todo_list_is_empty():
    todo_list = TodoList()
    result = todo_list.display_list()
    assert result == []