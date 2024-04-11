import streamlit as st
import to_do_app_functions

st.set_page_config(layout="wide")

todos = to_do_app_functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    to_do_app_functions.write_todos(todos)



st.title("Dipa's Todo App")
st.subheader("This is my todo app.")
st.write("This app is to manage your todo ")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        to_do_app_functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo... ",on_change=add_todo,
              key='new_todo')

st.session_state
print(st.session_state)