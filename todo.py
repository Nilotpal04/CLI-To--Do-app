import json
import os
tasks = []
if os.path.exists("tasks.json"):
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except json.JSONDecodeError:
        tasks = []
def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
while True:
    print("--ToDo-List--")
    print("1.Add task")
    print("2.View tasks")
    print("3.Mark task done")
    print("4.Delete task")
    print("5.Exit!")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter your task: ")
        task = {"task": task_name, "Done": False}
        tasks.append(task)
        save_tasks()
        print("Task added")
    elif choice == "2":
        print("\n--Your tasks--")
        for i, task in enumerate(tasks, 1):
            status = "✔️" if task["Done"] else "❌"
            print(f"{i}.{task['task']} - {status}")
    elif choice == "3":
        if not tasks:
            print("No tasks yet")
        else:
            print("\n--Your tasks--")
            for i, task in enumerate(tasks, 1):
                status = "✔️" if task["Done"] else "❌"
                print(f"{i}.{task["task"]} - {status}")
            try:
                task_num = int(input("Enter the task number to mark it as done: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["Done"] = True
                    save_tasks()
                    print("Task marked as done")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid number")
    elif choice == "4":
        if not tasks:
            print("No tasks yet")
        else:
            print("\n--Your tasks--")
            for i, task in enumerate(tasks, 1):
                status = "✔️" if task["Done"] else "❌"
                print(f"{i}.{task["task"]} - {status}")
        try:
            task_num = int(input("Enter the task number to delete it: "))
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                save_tasks()
                print("Task deleted!")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid number")
    elif choice == "5":
        print("Exiting the to do list! Bye...")
        break
    else:
        print("Invalid choice! Try again")

