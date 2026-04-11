from flask import Flask, jsonify

app = Flask(__name__)

items = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Phone"}
]

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item)

    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)