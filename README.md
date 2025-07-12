# Nash-odoo Hackthon
# 🔁 Skill Swap Platform

A full-stack web application that allows users to **exchange skills** with others in the community. This platform promotes **peer-to-peer learning** by matching people based on what they want to learn and what they can teach.

---
Team Leader:- Bhatt Jaymeen 
email:-jaymeenb123@gmail.com
Team Member 1:- Rudra vaishnav
email:-rudravaishnav148@gmail.com
Team Member 2:- Rajput Ritesh
email:-atulr9848@gmail.com
Team Member 3:- Aesvi Malaviya
email:-aesvimalaviya2237@gmail.com

## 🚀 Features

- 👤 User Registration & Login
- 🔐 Two-Factor Authentication (optional)
- 🧠 Create and Manage Skills
- 🔎 Browse Public Profiles
- 📬 Send & Manage Swap Requests
- 🌗 Light/Dark Mode Toggle
- 📨 Private Messaging System
- 🚩 Report Inappropriate Content
- 🛡️ Admin Control (optional)
- 🎨 Responsive UI with Tailwind CSS

---

## 📁 Folder Structure
skill_swap/
├── app/
│ ├── static/ # CSS, JS, images
│ ├── templates/ # HTML files
│ ├── routes/ # All Flask routes
│ ├── crud/ # CRUD operations
│ ├── models.py # SQLAlchemy models
│ ├── db.py # DB setup (SQLite + SQLAlchemy)
│ └── init.py # App factory
├── run.py # Main Flask run file
├── requirements.txt # All Python dependencies
└── README.md # This file


---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/skill_swap.git
cd skill_swap


2. Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run the Application
bash
Copy code
python run.py
The app will start on: http://127.0.0.1:5000

⚙️ Tech Stack
Frontend: HTML5, Tailwind CSS, JavaScript

Backend: Flask, Python

Database: SQLite + SQLAlchemy ORM

🧪 Usage
Register a new user account.

Add skills you want to teach or learn.

Search other profiles and send swap requests.

Manage your requests and messages from your profile.

Admin can view flagged content and handle moderation.


