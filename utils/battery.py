import psutil
import time
from utils.tray_icon import create_tray_icon

def get_battery_percentage():
    battery = psutil.sensors_battery()
    return battery.percent

def update_icon(icon):
    last_battery_percentage = get_battery_percentage()
    icon.icon = create_tray_icon(last_battery_percentage)
    while True:
        battery_percentage = get_battery_percentage()
        if last_battery_percentage != battery_percentage:
          icon.icon = create_tray_icon(battery_percentage)
          last_battery_percentage = battery_percentage
          time.sleep(30)
        else:
          time.sleep(10)