from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data
items = [
    {"id": 1, "name": "Laptop"}
]

# ✅ PUT: Update item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Invalid data"}), 400

    item = next((item for item in items if item["id"] == item_id), None)

    if item:
        item["name"] = data["name"]
        return jsonify(item), 200

    # Optional: create if not found
    new_item = {
        "id": item_id,
        "name": data["name"]
    }
    items.append(new_item)

    return jsonify(new_item), 201


if __name__ == '__main__':
    app.run(debug=True)