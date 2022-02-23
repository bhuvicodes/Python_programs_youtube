import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 50 and plugged != True:
    from pynotifier import Notification

    Notification(
        title = "Battery Low",
        description = str(percent) + "% Battery Remains!",
        duration  = 5,
    ).send()
    
