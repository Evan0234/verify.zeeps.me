from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.get_json()
    phone_number = data.get('phone')
    api_key = os.getenv('ABSTRACT_API_KEY')
    message = "This is a test message from verify.zeeps.me."

    if not phone_number:
        return jsonify({"message": "Phone number is required"}), 400

    url = f"https://sms.abstractapi.com/v1/?api_key={api_key}&phone={phone_number}&message={message}"
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify({"message": "Message sent successfully!"}), 200
    else:
        return jsonify({"message": f"Failed to send message. {response.text}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
