@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Invalid data"}), 400

    item = next((item for item in items if item["id"] == item_id), None)

    if item:
        item["name"] = data["name"]
        return jsonify(item), 200

    # Optional: create if not found (true PUT behavior)
    new_item = {
        "id": item_id,
        "name": data["name"]
    }
    items.append(new_item)

    return jsonify(new_item), 201