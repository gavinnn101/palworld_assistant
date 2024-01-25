import pyautogui
import keyboard
import threading

# GLOBALS
TOGGLE_KEY = "`"
END_KEY = "esc"
KEY_TO_HOLD = "f"

toggle = False


def on_triggered():
    global toggle
    toggle = not toggle

    if toggle:
        print(f"Holding {KEY_TO_HOLD} key...")
        pyautogui.keyDown(KEY_TO_HOLD)
    else:
        print(f"Releasing {KEY_TO_HOLD} key...")
        pyautogui.keyUp(KEY_TO_HOLD)


def listen():
    keyboard.add_hotkey(TOGGLE_KEY, on_triggered)

    print(f"Listening for key press... Press {TOGGLE_KEY} to toggle holding {KEY_TO_HOLD} key.")
    keyboard.wait(END_KEY)


def main():
    listen_thread = threading.Thread(target=listen)
    listen_thread.start()
    listen_thread.join()


if __name__ == "__main__":
    main()
