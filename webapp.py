import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_input = st.session_state["new_todo"] + '\n'
    todos.append(todo_input)
    functions.write_todos(todos)


st.title("To-do App")
#st.subheader("This is my to-do app")
st.text("Boost your productivity by keeping track of your todos")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a new todo here..",
              on_change=add_todo, key="new_todo")
