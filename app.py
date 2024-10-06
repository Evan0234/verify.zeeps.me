from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    api_key = os.getenv('ABSTRACT_API_KEY')
    phone_number = "14152007986"  # Hardcoded phone number

    # Step 1: Validate the Phone Number
    validation_url = f"https://phonevalidation.abstractapi.com/v1/?api_key={api_key}&phone={phone_number}"
    validation_response = requests.get(validation_url)
    validation_data = validation_response.json()

    if validation_response.status_code != 200 or not validation_data.get('valid'):
        return jsonify({"message": "Invalid phone number."}), 400

    # Step 2: Send SMS (update this part with the correct SMS endpoint and payload)
    sms_message = "This is a test message from verify.zeeps.me."
    sms_url = f"https://sms.abstractapi.com/v1/?api_key={api_key}&phone={phone_number}&message={sms_message}"
    sms_response = requests.get(sms_url)

    if sms_response.status_code == 200:
        return jsonify({"message": "Message sent successfully!"}), 200
    else:
        return jsonify({"message": f"Failed to send message. {sms_response.text}"}), sms_response.status_code

if __name__ == '__main__':
    app.run(debug=True)
