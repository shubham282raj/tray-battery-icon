import pystray
from utils.tray_menu import menu
from utils.battery import update_icon
import threading

icon = pystray.Icon("battery", None, "Battery Icon", menu)

thread = threading.Thread(target=update_icon, args=(icon,), daemon=True)
thread.start()

icon.run()