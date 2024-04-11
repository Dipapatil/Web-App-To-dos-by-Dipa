# Program to create a to do app, another python file created to_do_app_functions.py it has all the functions which are used in here.

import to_do_app_functions
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ",now)
while True:
    user_action = input("Type add, show, edit, complete(remove) or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        todos = to_do_app_functions.get_todos('todos.txt')

        todos.append(todo)
        to_do_app_functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = to_do_app_functions.get_todos()
        new_todos = [item.strip('\n') for item in todos ]
        for index, item in enumerate(new_todos):
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number-1

            todos = to_do_app_functions.get_todos()

            new_todo = input("Enter New todo : ")
            todos[number] = new_todo + '\n'

            to_do_app_functions.write_todos(todos)
        except ValueError:
            print("Not valid, please enter number to edit")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = to_do_app_functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            to_do_app_functions.write_todos(todos)

            print(f"Todo {todo_to_remove} was removed from the list")

        except IndexError:
            print("Not valid input")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
print("Bye Bye!!")




