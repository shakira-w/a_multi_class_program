# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self._list_of_todos = []

    def display_list(self):
        return self._list_of_todos

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self._list_of_todos.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        # incomplete_list = []
        # for todo in self._list_of_todos:
        #     if not todo.complete:
        #         incomplete_list.append(todo)
        # return incomplete_list
        return [todo for todo in self._list_of_todos if not todo.complete]

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        # complete_list = []
        # for todo in self._list_of_todos:
        #     if todo.complete:
        #         complete_list.append(todo)
        # return complete_list
        return [todo for todo in self._list_of_todos if todo.complete]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self._list_of_todos:
            if not todo.complete:
                todo.complete = True
