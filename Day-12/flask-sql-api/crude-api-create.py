from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DB CONFIG
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/flask_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# MODEL
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# CREATE TABLE
with app.app_context():
    db.create_all()

# POST API
@app.route('/task', methods=['POST'])
def add_task():
    data = request.get_json()   # 👈 important line

    new_task = Task(
        title=data['title'],
        done=data.get('done', False)
    )

    db.session.add(new_task)
    db.session.commit()

    return jsonify({"msg": "Task added successfully"})

# RUN
if __name__ == '__main__':
    app.run(debug=True)