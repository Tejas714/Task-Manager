# Task-Manager
🗂️ Task Management System (Django)

A simple Django-based Task Management application that allows users to create, update, delete, and restore tasks.
Deleted tasks are not lost permanently — they are moved to a history (restore) section, from where they can be restored or deleted forever.

This project is ideal for learning Django CRUD operations, soft-delete concepts, and basic project structure.

🚀 Features

✅ Create new tasks

📝 Update existing tasks

❌ Delete single tasks

🗑️ Delete all tasks at once

♻️ Restore deleted tasks

📜 View deleted task history

🔁 Restore all deleted tasks

🔥 Permanently delete tasks from history

🛠️ Tech Stack

Backend: Django

Frontend: HTML (Django Templates)

Database: SQLite3 (default Django DB)

Language: Python

📁 Project Structure
TaskManagement/
│
├── manage.py
├── db.sqlite3
│
├── TaskManagement/        # Project settings
│
├── myapp/                 # Main application
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── add1.html
│   │   ├── update.html
│   │   └── history.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py

📊 Database Models
Task Model

Stores active tasks.

name

title

description

status

deadline

created

updated

TaskRestore Model

Stores deleted tasks for restore/history purposes.

name

title

description

status

deadline

🔄 How Deletion Works (Important)

When a task is deleted:

It is moved to TaskRestore

This acts like a soft delete

From History, you can:

Restore the task back to active tasks

Delete it permanently

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/TaskManagement.git
cd TaskManagement

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install Django
pip install django

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Start the Server
python manage.py runserver

6️⃣ Open in Browser
http://127.0.0.1:8000/

🌐 URL Routes
URL	Description
/	Home – View all tasks
/add/	Add new task
/update/<id>	Update task
/delete/<id>	Delete task
/delete_all/	Delete all tasks
/history/	View deleted tasks
/restore/<id>	Restore task
/restore_all/	Restore all tasks
/delete_restore/<id>	Delete task permanently
/delete_history/	Clear history
📌 Learning Outcomes

Django CRUD operations

Model relationships & migrations

Soft delete & restore logic

Django URL routing

Template rendering

🧠 Future Improvements (Optional)

🔐 User authentication

🎨 Better UI (Bootstrap / Tailwind)

🔍 Search & filter tasks

📅 Priority & reminders

🗄️ PostgreSQL / MySQL support

🤝 Contributing

Pull requests are welcome!
Feel free to fork this project and improve it.

📜 License

This project is for learning and educational purposes.
