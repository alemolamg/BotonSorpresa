import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    Status = GPIO.input(24)
    if Status == False:
        print("Botón pulsado")
        time.sleep(0.2)
