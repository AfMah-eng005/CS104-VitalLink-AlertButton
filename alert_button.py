import time
import requests
import RPi.GPIO as GPIO

BOT_TOKEN = "8649277640:AAHGa4XFNaa4UDdvRVGsIhYyd3ue2tHoIjA"
CHAT_ID = "8932215700"
URL = f"https://api.telegram.org/bot8649277640:AAHGa4XFNaa4UDdvRVGsIhYyd3ue2tHoIjA/sendMessage"

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

while True:
    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone pressed the alert button!")

        # Send Telegram message
        data = {
            "chat_id": CHAT_ID,
            "text": "Someone pressed the alert button!"
        }
        requests.post(URL, json=data)

        button_pressed = True

    elif GPIO.input(7) == GPIO.LOW:
        button_pressed = False

    time.sleep(0.1)

