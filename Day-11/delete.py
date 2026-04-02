from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data
items = [
    {"id": 1, "name": "Laptop"},
    {"id": 2, "name": "Phone"}
]

# ✅ REAL DELETE (API)
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items

    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return jsonify({
                "status": "success",
                "message": "Item deleted"
            })

    return jsonify({
        "status": "error",
        "message": "Item not found"
    }), 404


# BROWSER DELETE (for testing)
@app.route('/delete/<int:item_id>', methods=['GET'])
def delete_item_browser(item_id):
    global items

    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return f"Item with ID {item_id} deleted successfully ✅"

    return f"Item with ID {item_id} not found ❌"


# Optional: check items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


if __name__ == "__main__":
    app.run(debug=True)