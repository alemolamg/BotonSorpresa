import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#GPIO.setup(24, GPIO.IN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
count = 0
while True:
    inputValue = GPIO.input(24)
    if (inputValue == False):  # Cambiar el contenido del if por
        #count = count + 1
        #print("Button pressed " + str(count) + " times.")
        print("Botón pulsado")
        # time.sleep(0.3)
    time.sleep(.01)
