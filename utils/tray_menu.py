from pystray import MenuItem
import sys

def on_click(icon, item): 
  if str(item) == 'Quit':
    icon.stop()
    sys.exit(0)

menu = (
  MenuItem('Quit', on_click),
)