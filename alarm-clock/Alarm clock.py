#Python program for Simple Alarm Clock

#pip install pygame
from datetime import datetime
import time
import pygame

#asking the user for the time when the alarm will go off.
alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ") #example : 08:42:30 PM

#validating the user-provided time
def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"

#Calling our function
while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")

    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break

#separately storing the values into different variables
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

#a loop so that it keeps executing until our alarms rings.
while True:
    #getting the current time to compare it with the user-provided time.
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")
    #playing Sound
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Wake Up!")
                    pygame.mixer.init()
                    pygame.mixer.music.load("alarm-clock/DIA.wav") #replace filename with yours (wav format )
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    time.sleep(5)
                    exit()
