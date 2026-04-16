from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DB CONFIG
# Ensure your database 'flask_database' actually exists in Postgres
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/flask_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# MODEL
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# GET API
@app.route('/task', methods=['GET'])
def get_tasks():
    # .all() works, but it's good practice to handle empty results
    tasks = Task.query.all()

    task_list = [
        {'id': t.id, 'title': t.title, 'done': t.done}
        for t in tasks
    ]

    return jsonify(task_list)

# RUN
if __name__ == '__main__':
    # CRITICAL: Create the tables if they don't exist
    # This must be done within the app context
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)