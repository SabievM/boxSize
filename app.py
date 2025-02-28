import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_numbers', methods=['POST'])
def process_numbers():
    data = request.get_json()

    if not data or "numbers" not in data or not isinstance(data["numbers"], list) or len(data["numbers"]) != 3:
        return jsonify({"error": "Передай три числа в массиве"}), 400

    width, height, depth = data["numbers"]

    result = [
        0, 0, 0,
        0, height, 0,
        width, height, 0,
        width, 0, 0,
        0, 0, depth,
        0, height, depth,
        width, height, depth,
        width, 0, depth
    ]

    return jsonify({"success": True, "sent": result})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
