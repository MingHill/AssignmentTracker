from flask import Flask, render_template, url_for, request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#env/bin/activate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Todo(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    due_date = db.Column(db.DateTime)
    course = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id 


@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == 'POST': 
        task_content = request.form['content']
        task_course = request.form['course']

        if not task_content: 
            return "Task cannot be empty"
        
        
        try:
            task_due_date = datetime.strptime(request.form['due_date'], "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."
        
        if task_due_date < datetime.now(): 
            return "Due date must be in the future"
        
        if not task_course: 
            return "Course cannot be empyt"
        
        new_task = Todo(content = task_content, due_date = task_due_date, course = task_course)

        try: 
            db.session.add(new_task) 
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue addding your task"

    else: 
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks)
    
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try: 
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except: 
        return "There was a problem deleting that task"


@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content'] 
        task.due_date = datetime.strptime(request.form['due_date'], "%Y-%m-%d")
        task.course = request.form['course']

        if not task.content: 
            return "Task cannot be empty"
        
        if task.due_date < datetime.now(): 
            return "Due date must be in the future"
        
        if not task.course: 
            return "Course cannot be empyt"

        try: 
            db.session.commit()
            return redirect('/')
        except: 
            return "There was an issue updating your task"
    else: 
        return render_template('update.html', task = task)

if __name__ == "__main__":
    app.run(debug = True)