# 📝 CLI To-Do List App

A simple command-line based To-Do List built in Python.  
Supports adding, viewing, marking as done, deleting tasks — with persistent storage using JSON.

---

## 🚀 Features
- Add tasks with status
- View all tasks with done/undone icons
- Mark tasks as done
- Delete specific tasks
- Saves tasks to a `tasks.json` file (persistent)

---

## 🛠️ Tech Stack
- Python 3
- JSON for data storage
- CLI-based interface

---

## 💡 How to Run

1. Clone the repo or copy the code.
2. Make sure Python 3 is installed.
3. Run the app:
```bash
python todo.py
```

---

## 📂 File Structure
```
todo.py         # Main app
tasks.json      # Automatically created to store tasks
```

---

## ✨ Sample Output
```
--ToDo-List--
1.Add task
2.View tasks
3.Mark task done
4.Delete task
5.Exit!
```

---

## 🔒 Data Storage
Tasks are stored as a list of dictionaries in `tasks.json`:
```json
[
  {
    "task": "Finish homework",
    "Done": false
  }
]
```

---

## 🙌 Author
Made with 💻 by Nlotpal
