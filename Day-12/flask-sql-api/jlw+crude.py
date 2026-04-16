from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

# DB CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/flask_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT CONFIG
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db = SQLAlchemy(app)
jwt = JWTManager(app)

# MODEL
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# CREATE TABLE
with app.app_context():
    db.create_all()

# 🔐 LOGIN API
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if data['username'] == 'admin' and data['password'] == 'admin':
        token = create_access_token(identity='admin')
        return jsonify(access_token=token)

    return jsonify({"msg": "Invalid credentials"}), 401

# 🟢 GET (READ)
@app.route('/task', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()
    task_list = [
        {'id': t.id, 'title': t.title, 'done': t.done}
        for t in tasks
    ]
    return jsonify(task_list)

# 🟢 POST (CREATE)
@app.route('/task', methods=['POST'])
@jwt_required()
def add_task():
    data = request.get_json()

    new_task = Task(
        title=data['title'],
        done=data.get('done', False)
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({"msg": "Task added"})

# 🟢 PUT (UPDATE)
@app.route('/task/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"msg": "Task not found"}), 404

    data = request.get_json()

    task.title = data.get('title', task.title)
    task.done = data.get('done', task.done)

    db.session.commit()

    return jsonify({"msg": "Task updated"})

# 🔴 DELETE
@app.route('/task/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    task = Task.query.get(id)

    if not task:
        return jsonify({"msg": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"msg": "Task deleted"})

# RUN
if __name__ == '__main__':
    app.run(debug=True)