from pystray import MenuItem

def on_click(icon, item): 
  if str(item) == 'Quit':
    icon.stop()

menu = (
  MenuItem('Quit', on_click),
)