# this functions used in python file todo_app_dipa.py

FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items.  """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

#print("value of __name__ : ",__name__)
def write_todos(todos_arg,filepath=FILEPATH):
    """
    Write the file todos.txt
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Inside main")
    print(get_todos())