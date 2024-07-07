

task_list = []

def add_task(new_task):
    task_list.append(f"{new_task}: incomplete")
    print(f"Great, {new_task} added to your To-Do List")

def view_tasks():
    print("Your To-Do list is as follows: ")
    if len(task_list) == 0:
        print("Nothing To Do!")
    else:
        for task in task_list:
            print(f"{task}")

def task_complete(completed_task):
         task_list.remove(f"{completed_task}: incomplete")
         task_list.append(f"{completed_task}: complete")
         print(f"{completed_task} has been marked complete!")

def delete_task(task):
    try:    
        task_list.remove(task)
        print(f"{task} has been deleted")
    except ValueError:
        print(f"{task} is not in your To- Do List!")


while True:
    try:
        command_choice = int(input("Welcome to the To-Do List App! \n\nMenu: \n1. Add a task \n2. View tasks \n3. Mark a task as complete \n4. Delete a task \n5. Quit \n\nPlease enter a number 1-5: "))
    except ValueError:
         print("Try again and choose a number 1-5")
         break
    if command_choice == 1:
        try:
            new_task = input("What is your new task? ")
            add_task(new_task)
        except f"{new_task}: incomplete" in task_list:
             print("That task is already in here")
    elif command_choice == 2:
        try:
            view_tasks()
        except: 
             pass
    elif command_choice == 3:
        try:
            completed_task = input("What task would you like to mark as complete: ")
            if f"{completed_task}: incomplete" in task_list:
                task_complete(completed_task)
            else:
               print("That activity was not found in your To-Do List or is already complete!") 
        except:
            pass
    elif command_choice == 4:
           deleted_task = input("Which task would you like to delete?")
           if f"{deleted_task}: incomplete" in task_list:
                delete_task(f"{deleted_task}: incomplete")
           elif f"{deleted_task}: complete" in task_list:
                delete_task(f"{deleted_task}: complete")
    elif command_choice == 5:
        try:
            print("Toodaloo, thanks for to-doing!")
            break
        except:
             pass
    else:
        print("Invalid input, please print a number 1-5: ")