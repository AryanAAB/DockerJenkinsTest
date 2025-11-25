import sys
import json
import os

DATA_FILE = "todo_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(task):
    tasks = load_data()
    tasks.append({"task": task, "done": False})
    save_data(tasks)
    print(f"Added: {task}")

def list_tasks():
    tasks = load_data()
    if not tasks:
        print("No tasks found.")
        return
    for idx, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✗"
        print(f"{idx}. [{status}] {t['task']}")

def mark_done(index):
    tasks = load_data()
    if 0 < index <= len(tasks):
        tasks[index-1]["done"] = True
        save_data(tasks)
        print("Task marked as done.")
    else:
        print("Invalid index")

def delete_task(index):
    tasks = load_data()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index-1)
        save_data(tasks)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid index")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python todo.py add <task>")
        print("  python todo.py list")
        print("  python todo.py done <index>")
        print("  python todo.py del <index>")
        return

    command = sys.argv[1]

    if command == "add":
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "done":
        mark_done(int(sys.argv[2]))
    elif command == "del":
        delete_task(int(sys.argv[2]))
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
