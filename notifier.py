import sys
from pynotifier import Notification
from datetime import datetime


path = "<path to the directory of the images logo>"

def sendmessage(message, icon):
    Notification(
	    title=message,
	    icon_path=path + icon,
	    duration=10,                              
	    urgency='normal'
    ).send()

def switch_icon(task):
    switch = {
        "Task1": "try.png",
        "Task2": "sun.png",
        "Task3": "code_wars.png",
        "Task4": "sun.png",
        "Task5": "work.png",
        "Task6": "exercise.png"
    }
    return switch[task]

if __name__ == '__main__':
    finish = False
    # Mount your schedule with your task's and time 
    schedule = {
        "7:00": "Task1",
        "10:00": "Task2",
        "10:10": "Task3",
        "11:30": "Task4",
        "14:00": "Task5",
        "18:00": "Task6"
    }
    sendmessage(schedule["18:00"], switch_icon(schedule["18:00"]))
    sys.exit()
    while not finish:
        current_time = datetime.now().strftime('%H:%M')
        if schedule.keys() == current_time:
            sendmessage(schedule[current_time], switch_icon(schedule[current_time]))
