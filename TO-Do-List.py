from pathlib import Path

def load_tasks():
    tasks = []
    file_path = Path("To-Do-List.txt")
    if file_path.exists():
        with file_path.open("r") as f:
            for line in f:
                try:
                    task, done = line.rsplit(" - ", 1)
                    done = done.strip() == "done"
                    tasks.append({"task": task, "done": done})
                except ValueError:
                    continue  # Skip malformed lines
    return tasks

def save_tasks(tasks):
    with Path("To-Do-List.txt").open("w") as f:
        for task in tasks:
            status = "done" if task["done"] else "not done"
            f.write(f"{task['task']} - {status}\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)

def mark_done(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        save_tasks(tasks)
        print("Task marked as done.")
    else:
        print("Invalid task index")

def delete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task index")

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            status = "done" if task["done"] else "not done"
            print(f"{i}. {task['task']} - {status}")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1] Add task")
        print("2] Mark task as done")
        print("3] Delete task")
        print("4] Show tasks")
        print("5] Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                task = input("Enter task: ")
                add_task(task)
            case "2":
                try:
                    task_index = int(input("Enter task index to mark as done: "))
                    mark_done(task_index)
                except ValueError:
                    print("Please enter a valid number.")
            case "3":
                try:
                    task_index = int(input("Enter task index to delete: "))
                    delete_task(task_index)
                except ValueError:
                    print("Please enter a valid number.")
            case "4":
                show_tasks()
            case "5":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()
