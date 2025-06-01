import pyautogui
import time
from pynput import keyboard

TEXT_TO_TYPE = "text"
TYPING_DELAY = 0.02
HOTKEY = {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.Key.shift, keyboard.KeyCode(char='g')}
current_keys = set()

def type_string(text):
    try:
        time.sleep(1)
        for char in text:
            pyautogui.typewrite(char)
            time.sleep(TYPING_DELAY)
        print("finished")
    except Exception as e:
        print(f"Error: {e}")

def on_press(key):
    if key in HOTKEY:
        current_keys.add(key)
        if all(k in current_keys for k in HOTKEY):
            type_string(TEXT_TO_TYPE)
    elif key == keyboard.Key.esc:
        print("Exiting...")
        return False

def on_release(key):
    if key in current_keys:
        current_keys.remove(key)

def main():
    print("Hotkey: ctrl + option + Shift + G")
    print("Press esc to exit.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()