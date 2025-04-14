![Screenshot 2025-04-14 215306](https://github.com/user-attachments/assets/f6ed5071-7fc3-44b4-8d37-2e1427b97cc3)


## 📝 To-Do List CLI App

A simple command-line To-Do List manager built in Python. You can add, view, and remove tasks with ease. Designed for beginners to get comfortable with Python basics and file handling.

---

### ⚙️ Features

- ➕ Add new tasks  
- 📋 View all tasks  
- ❌ Remove tasks (case-insensitive)  
- 💾 (Optional) Expand with file save/load functionality  

---

### 🖥️ How to Use

#### 1. **Run the program**
```bash
python todo.py
```

#### 2. **Choose an option**
```
1. Add a task  
2. View tasks  
3. Remove a task  
4. Exit  
```

---

### 🧠 Example Interaction
```bash
Enter your choice: 1  
Enter the task: Buy groceries  
Task added!

Enter your choice: 2  
Your tasks:  
1. Buy groceries  

Enter your choice: 3  
Enter the task to remove: buy groceries  
Task removed
```

---

### 💡 Case-Insensitive Task Removal

When removing a task, the app will match your input regardless of case:
- Typing `buy groceries` will remove `Buy Groceries`

---

### 🛠️ Future Enhancements (Optional)
- Save/load tasks to a text file  
- Add deadlines or priorities  
- GUI version with Tkinter or Streamlit  

---

### 📁 File Structure
```
todo.py        # Main CLI app
README.md      # You're here!
```

---

### 🧑‍💻 Author
Pulkit Mathur 

---
---
