import pyautogui, keyboard, sys, threading, time, random, os
from datetime import datetime, timedelta


def start_by_path(app):
    if os.getlogin() == 'krawc':
        tem = r"D:\Apps\MSTeamsSetup_c_l_.exe"
        out = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Outlook.lnk"
    else:
        tem = fr"C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams classic.lnk"
        out = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Outlook.lnk"

    if app == "Teams":
        os.startfile(tem)
    elif app == "Outlook":
        os.startfile(out)


def mouse_move(x, y):
    speeds = [0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]
    pyautogui.moveTo(x, y, random.choice(speeds))
    pyautogui.click()


def outlook(end):
    x = 325
    y = 350
    start = datetime.now()

    start_by_path("Outlook")
    time.sleep(5)

    mouse_move(x, y)
    time.sleep(1)

    while True:
        process_time = datetime.now() - start
        if process_time >= end:
            break

        mouse_move(x, random.randint(300, 900))
        time.sleep(1)
        pyautogui.press('space')


def teams(end):
    x = 450
    y = 50
    start = datetime.now()

    start_by_path("Teams")
    time.sleep(5)

    mouse_move(x, y)
    time.sleep(1)
    pyautogui.hotkey('ctrl', '2')

    while True:
        process_time = datetime.now() - start
        if process_time >= end:
            break

        mouse_move(x, random.randint(400, 800))
        time.sleep(1)


def exit_listening():
    while True:
        if keyboard.is_pressed('F7'):
            sys.exit()


def apps_launch():
    while True:
        teams(timedelta(seconds=300))
        outlook(timedelta(seconds=300))


if __name__ == "__main__":
    threading.Thread(target=exit_listening, name='killer', daemon=False).start()
    threading.Thread(target=apps_launch, name='apps', daemon=True).start()
