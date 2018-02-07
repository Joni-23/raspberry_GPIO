from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class room_alerts:
    def __init__(self,pin,msg):
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=self.int_func, bouncetime=300) 

        self.__pin = pin;
        self.__msg = msg;

    def int_func(self, pin_number):
        print("Interrupt happend in:",pin_number," port")
        print(self.__msg)

alarmlist = []

def add_pins():
    pin_list = open("pin_list","r")

    for lines in pin_list.readlines():
        pin_number = ""
        for char in lines:
            if(char == '\t'):
                pin = int(pin_number)
                msg = lines[len(pin_number)+1:]
                alarmlist.append(room_alerts(pin,msg))
                break
            else:
                pin_number += char



add_pins()
while(1):
    sleep(1)
