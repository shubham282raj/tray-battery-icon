import psutil
import time
from utils.tray_icon import create_tray_icon

def get_battery_color(battery):
    if battery.power_plugged:
        return 'green'
    elif battery.percent > 20:
        return 'white'
    else:
        return 'red'

def update_icon(icon):
    last_percentage, last_power = -1, -1
    while True:
        battery = psutil.sensors_battery()
        if not (last_percentage == battery.percent and last_power == battery.power_plugged):
            color = get_battery_color(battery)
            icon.icon = create_tray_icon(battery.percent, color)
            last_percentage, last_power = battery.percent, battery.power_plugged
        time.sleep(1)