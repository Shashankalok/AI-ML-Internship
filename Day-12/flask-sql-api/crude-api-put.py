from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# 1. Define the app FIRST
app = Flask(__name__)

# 2. Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/flask_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. Initialize the database SECOND
db = SQLAlchemy(app)

# 4. Define your Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# 5. Define your routes AFTER 'app' is defined
@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = db.session.get(Task, task_id)
    
    if not task:
        return jsonify({"message": "Task not found"}), 404

    data = request.get_json()
    
    # Update fields
    task.title = data.get('title', task.title)
    task.done = data.get('done', task.done)

    db.session.commit()
    
    return jsonify({
        "id": task.id,
        "title": task.title,
        "done": task.done
    })

# 6. Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)