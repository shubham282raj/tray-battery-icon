import pystray
from utils.tray_icon import create_tray_icon
from utils.tray_menu import menu

icon = pystray.Icon("battery", create_tray_icon(17), "Battery Icon", menu)
icon.run()