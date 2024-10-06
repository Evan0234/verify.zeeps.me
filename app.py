from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/validate_phone', methods=['GET'])
def validate_phone():
    # Retrieve API key from environment variables
    api_key = os.getenv('ABSTRACT_API_KEY')
    phone_number = "14152007986"  # Hardcoded phone number

    # Call the Abstract API to validate the phone number
    validation_url = f"https://phonevalidation.abstractapi.com/v1/?api_key={api_key}&phone={phone_number}"
    response = requests.get(validation_url)

    if response.status_code == 200:
        return jsonify({"message": "Phone number validated successfully!"}), 200
    else:
        return jsonify({"message": f"Failed to validate phone number. Status code: {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
