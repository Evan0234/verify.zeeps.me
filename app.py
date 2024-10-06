from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.get_json()
    phone_number = data.get('phone')

    # Retrieve API key from environment variables (from GitHub Secrets)
    api_key = os.getenv('ABSTRACT_API_KEY')
    message = "This is a test message from the Abstract API!"  # Your message content

    # Call the Abstract API to send the SMS
    sms_url = f"https://sms.abstractapi.com/v1/?api_key={api_key}&phone={phone_number}&message={message}"
    response = requests.get(sms_url)

    if response.status_code == 200:
        return jsonify({"message": "Message sent successfully!"}), 200
    else:
        return jsonify({"message": f"Failed to send message. Status code: {response.status_code}, Error: {response.text}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
