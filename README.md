# 📝 To-Do List App

A simple, command-line-based To-Do List application that helps you manage tasks effectively. <br>
This project is built with Python and features task management options such as adding tasks, viewing the task list, marking tasks as complete, and deleting tasks. <br>
 Tasks are saved in a JSON file, so your to-do list persists even when you close and reopen the app. <br>

## 🚀 Features

- **Add New Tasks**: Quickly add new tasks to your list.
- **View All Tasks**: See all tasks along with their status (Pending or Done).
- **Mark Tasks as Complete**: Keep track of completed tasks.
- **Delete Tasks**: Remove tasks that are no longer needed.
- **Persistent Storage**: Saves tasks to a `tasks.json` file, so your list remains even if you close the app.

## 🛠️ Installation & Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/todo-list-app.git
    cd todo-list-app
    ```

2. **Run the application**:
    ```bash
    python todo_list.py
    ```

3. **Use the menu**:
   - Follow the on-screen prompts to add, view, complete, or delete tasks.

## 📖 How It Works

The application uses a JSON file (`tasks.json`) to save tasks persistently. Each task is stored as a dictionary in a list, with the following structure:

```json
{
  "description": "Sample task description",
  "completed": false
}
```
## 🧩 Future Enhancements

Here are some potential improvements you could add to the project:

- **Task Prioritization:** Add levels of priority for each task.
- **Due Dates:** Allow users to set a due date for tasks.
- **Categories:** Organize tasks by category (work, personal, etc.).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/leshokefa/RockPaperScissorsByLesho/issues).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy playing! If you like this project, please give it a ⭐ on GitHub!

---
