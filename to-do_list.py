# W6 S3 - Challenge

import json
import os

# Load tasks from the JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Program structure in a loop to display menu to the user
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = int(input("\nEnter option: "))
        while choice not in [1, 2, 3, 4, 5]:
            print("\n// Error! Invalid option. Please try again //")
            choice = int(input("\nEnter option: "))

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
            input("Press enter to continue")
            screen_refresh()
        elif choice == 3:
            update_task(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            break

# Clearing screen
def screen_refresh():
    os.system("cls")


# Creating a new task
def add_task(tasks):
    description = ""
    while not description:
        description = input("\nEnter task description: ").title()
        if description == "":
            print("// Error! Invalid description. Please try again //")

    status = input("Enter task status (Incomplete/Completed): ").upper()
    if status == "":
        status = "Incomplete".upper()
    task = {"description": description, "status": status}
    tasks.append(task)
    save_tasks(tasks)
    input("\n// Task added successfully //")
    screen_refresh()

# Viewing all tasks
def view_tasks(tasks):
    if not tasks:
        print("// No tasks available //")
        return
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['description']}      // {task['status']} //")
        

# Updating a task
def update_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("\nEnter the task number to update: ")) - 1
        while task_index not in range(len(tasks)):
            print("\n// Error! Invalid task number //")
            task_index = int(input("\nEnter the task number to update: ")) - 1

        if task_index < 0 or task_index >= len(tasks):
            raise IndexError
        description = input("Edit description: ")
        status = input("Edit status (Incomplete/Completed): ").upper()
        if status == "":
            status = "Incomplete".upper()
        if description:
            tasks[task_index].update({"description": description, "status": status})
        else:
            tasks[task_index].update({"status": status})
        save_tasks(tasks)
        input("\n// Task updated successfully //")
        screen_refresh()
    except (ValueError, IndexError):
        input("\n// Error! Invalid task number //")
        screen_refresh()

# Deleting a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("\nEnter the task number to delete: ")) - 1
        while task_index not in range(len(tasks)):
            print("\n// Error! Invalid task number //")
            task_index = int(input("\nEnter the task number to delete: ")) - 1

        if task_index < 0 or task_index >= len(tasks):
            raise IndexError
        tasks.pop(task_index)
        save_tasks(tasks)
        input("\n// Task deleted successfully //")
        screen_refresh()
    except (ValueError, IndexError):
        input("\n// Error! Invalid task number //")
        screen_refresh()

if __name__ == "__main__":
    main()