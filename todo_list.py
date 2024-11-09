import json

tasks = []

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    description = input("Enter task description: ")
    task = {"description": description, "completed": False}
    tasks.append(task)
    print("\nTask added!")
    save_tasks()

def view_tasks():
    if not tasks:
        print("\nNo tasks found.")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['description']} - {status}")

def complete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        tasks[task_number - 1]["completed"] = True
        print("\nTask marked as complete!")
        save_tasks()
    except (ValueError, IndexError):
        print("\nInvalid task number.")

def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        tasks.pop(task_number - 1)
        print("\nTask deleted!")
        save_tasks()
    except (ValueError, IndexError):
        print("\nInvalid task number.")

def show_menu():
    print("\nTo-Do List App\n")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit\n")

load_tasks()

while True:
    
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
