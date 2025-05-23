import streamlit as st
import functions

todos = functions.get_todos()

st.title("To-do App")
#st.subheader("This is my to-do app")
st.text("Boost your productivity by keeping track of your todos")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a new todo here..")

