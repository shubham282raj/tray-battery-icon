import psutil
import time
from utils.tray_icon import create_tray_icon

def get_battery_percentage():
    battery = psutil.sensors_battery()
    return battery.percent

def update_icon(icon):
    while True:
        battery_percentage = get_battery_percentage()
        icon.icon = create_tray_icon(battery_percentage)
        time.sleep(30)