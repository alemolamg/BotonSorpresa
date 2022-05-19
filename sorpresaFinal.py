import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    Status = GPIO.input(24)
    if Status == False:  # Boton pulsado
        print("Botón pulsado")
        os.system('mpg123 ./audio/audioSorpresa.mp3')
        time.sleep(0.2)
