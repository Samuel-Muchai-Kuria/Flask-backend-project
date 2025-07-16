## 🧼 Flask Fullstack App

This is a simple full-stack web application built with Flask. It includes user authentication and renders all pages using server-side HTML templates.

### 🔗 Live Deployment
[View on Render](https://flask-backend-project-95yk.onrender.com/)

### 🔧 Features
- User registration and login
- Password hashing
- SQLite database with SQLAlchemy
A Flask-based web application with secure user authentication and dynamic meme generation on login. User data is stored in an SQL database, and the frontend is built with HTML, CSS, and JavaScript.

> 🚧 **Note:** This project is currently a work in progress.

## 🔐 Features

- User registration and login
- Authentication system with session management
- Secure user data storage in SQL 
- Meme generation after successful login
- Responsive frontend using HTML, CSS, and JavaScript

## ⚙️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQL (SQLite by default)
- **Authentication:** Flask-Login 

## 📦 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Flask-backend-project.git
   cd Flask-backend-project
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   flask run
   ```

5. **Access in browser:**

   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
project/
│
├── static/             # CSS, JavaScript, images
├── templates/          # HTML templates
├── app.py              # Main Flask application
├── database.db         # SQL database (example for SQLite)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## 🚀 To Do

* [ ] Finalize frontend styling
* [ ] Add form validation
* [ ] Improve meme generation logic
* [ ] Implement user profile pages
* [ ] Deploy to hosting platform (frontend on vercel and backend on Render)

## 📄 License

This project is licensed under the [MIT License](LICENSE).

⚡ Note: This project was built by combining and modifying components from various YouTube tutorials. The user authentication flow was inspired by YouTube tutorial on Flask login, and the meme generation logic was also adapted from YouTube tutorial on meme creation. I integrated and customized these features into a single working application as part of my learning process.
