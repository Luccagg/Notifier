
# Desktop Notifier

. You put in the schedule dict your task and the time that task begin.
. The script gonna run on the background (crontab on Linux) and gonna run every day at 6am
. When the current time is equal to the time that a task start, the script will popup an alert with the name of your task. You can add a icon for each task, only need to modify the path and concatenate with the name of the icon image (i.e code.png)


##Requirements
.py-notifier --> pip3 install py-notifier
.libnotify-bin --> sudo apt-get install libnotify-bin (LINUX)

