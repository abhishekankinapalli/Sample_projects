
# command-line to-do list application to manage tasks.

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number.")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        task = input("Enter a task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        index = int(input("Enter task number to remove: "))
        remove_task(index)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Try again.")
