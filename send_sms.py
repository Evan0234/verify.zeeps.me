import requests
import os

def send_test_message(phone_number, message):
    api_key = os.getenv('ABSTRACT_API_KEY')
    url = f"https://sms.abstractapi.com/v1/?api_key={api_key}&phone={phone_number}&message={message}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Error: {response.text}")

if __name__ == "__main__":
    phone_number = input("Enter the phone number to send a message: ")
    message = "This is a test message from verify.zeeps.me."
    send_test_message(phone_number, message)
