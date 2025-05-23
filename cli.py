import functions
import time
import os

if not os.path.exists("todos.txt"):
	with open("todos.txt", 'w') as file:
		pass

now = time.strftime("%b-%d, %y %H:%M:%S")
print("It is", now)
while True:
	user_action = input("Enter add, show, edit, complete, or exit: ")
	user_action = user_action.strip()


	if user_action.startswith("add"):
		todo = user_action[4:]
		todos = functions.get_todos()
		todos.append(todo + '\n')

		functions.write_todos(todos)

	elif user_action.startswith("show"):

		todos = functions.get_todos()

		for index, item in enumerate(todos):
			item = item.strip('\n')
			row = f"{index + 1}-{item}"
			print(row)

	elif user_action.startswith('edit'):
		try:
			number = int(user_action[5:])
			number = number - 1
			todos = functions.get_todos()
			new_todo = input("Enter a new todo: ")
			todos[number] = new_todo + "\n"
			functions.write_todos(todos)
		except ValueError:
			print("Your command is not valid")
			continue

	elif user_action.startswith('complete'):
		try:
			number = int(user_action[9:])

			todos = functions.get_todos()
			index = number - 1
			todo_to_remove = todos[index].strip('\n')
			todos.pop(index)
			todos = functions.get_todos()
			row = f"the todo {todo_to_remove} has been completed"
		except IndexError:
			print("There is no todo with that number")
			continue
	elif user_action.startswith('exit'):
		break
	else:
		print("Command is not valid.")
print("Bye!")