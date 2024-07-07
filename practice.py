

task_list = []

def add_task(task):
    task_list.append(task)

def view_tasks():
    print[task_list]

def task_complete():
    pass

def delete_task():
    pass


while True:
    command_choice = int(input("Welcome to the To-Do List App! \n\nMenu: \n1. Add a task \n2. View tasks \n3. Mark a task as complete \n4. Delete a task \n5. Quit \n\nPlease enter a number 1-5: "))
    if command_choice == 1:
        try:
            new_task = input("What is your new task? ")
            add_task(new_task)
            print(f"Great, {new_task} added to your To-Do List")
        except ValueError:
            print("Words only please")
    elif command_choice == 2:
        try:
            view_tasks()
        except:
            pass
    elif command_choice == 3:
        try:
            view_tasks()
        except:
            pass


    

