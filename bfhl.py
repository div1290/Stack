from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample user data (these would typically come from a database)
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

# POST method to handle user input
@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        # Get JSON data from the request
        data = request.get_json()
        data_list = data.get("data", [])

        # Separate numbers and alphabets
        numbers = [item for item in data_list if item.isdigit()]
        alphabets = [item for item in data_list if item.isalpha()]

        # Find the highest lowercase alphabet
        lower_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase_alphabet = max(lower_alphabets) if lower_alphabets else None

        # Prepare the response
        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 400

# GET method to return the operation code
@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
