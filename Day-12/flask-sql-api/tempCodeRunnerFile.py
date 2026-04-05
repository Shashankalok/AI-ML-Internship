from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] ='postgresql://postgres:Qwerty@123@localhost:5432/flask_databse'

db = SQLAlchemy(app)

# MODEL
class Task(db.Model):
    #__table__='tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# CREATE TABLE
with app.app_context():
    db.create_all()

@app.route('/task')
def index():
    tasks = Task.query.all()
    task_list = [
        {'id': task.id, 'title' : task.title}, 'done':task.done} for task in tasks
    ]
    return jsonify({"tasks": "task_list"})
    

if __name__=='__main__':
    app.run(debug=True)