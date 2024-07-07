

task_list = []

def add_task(task):
    task_list.append(task)


while True:
    command_choice = input("Welcome to the To-Do List App! \n\nMenu: \n1. Add a task \n2. View tasks \n3. Mark a task as complete \n4. Delete a task \n5. Quit \n\nPlease enter a number 1-5: ")
    if command_choice == 1:
        new_task = input("What is your new task? ")
        add_task(new_task)
    else:
        break