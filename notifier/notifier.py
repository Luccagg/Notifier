import sys
from pynotifier import Notification
from datetime import datetime


path = "/home/viper/Imagens/"

def sendmessage(message, icon):
    Notification(
	    title=message,
	    icon_path=path + icon,
	    duration=10,                              
	    urgency='normal'
    ).send()

def switch_icon(task):
    switch = {
        "TryHackMe": "try.png",
        "Break": "sun.png",
        "Code Wars": "code_wars.png",
        "Free": "sun.png",
        "Work": "work.png",
        "Exercise": "exercise.png"
    }
    return switch[task]

if __name__ == '__main__':
    finish = False
    schedule = {
        "7:00": "TryHackMe",
        "10:00": "Break",
        "10:10": "Code Wars",
        "11:30": "Free",
        "14:00": "Work",
        "18:00": "Exercise"
    }
    sendmessage(schedule["18:00"], switch_icon(schedule["18:00"]))
    sys.exit()
    while not finish:
        current_time = datatime.now().strftime('%H:%M')
        if schedule.keys() == current_time:
            sendmessage(schedule[current_time], switch_icon(schedule[current_time]))