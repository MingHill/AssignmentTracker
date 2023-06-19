Assignment Tracker

Assignment Tracker is a simple web application built with Flask that allows users to manage their assignments. It provides features to add, update, and delete tasks, along with a dashboard view to display all tasks in a tabular format.

Features
- Add new tasks with details like task content, due date, and course.
- Update existing tasks with modified details.
- Delete tasks from the dashboard.
- View all tasks in a tabular format.
- Client-side validation for task input fields.
- SQLite database integration to store tasks persistently.

Prerequisites
- Python 3.x
- Flask framework
- Flask SQLAlchemy extension

Installation
1. Clone the repository:
git clone https://github.com/MingHill/AssignmentTracker.git
2. Change into the project directory:
cd assignmentTrack
3. Create a virtual environment (optional but recommended):
python3 -m venv env
source env/bin/activate
4. Install the required dependencies:
pip install -r requirements.txt

Usage
Start the Flask development server:
python app.py
Access the application in your web browser at http://localhost:5000.

Use the web interface to add, update, and delete tasks.

