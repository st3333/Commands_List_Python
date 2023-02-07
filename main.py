import os
import pyautogui as pg
import cv2

while True:
    commands = input('Command: ')

    if commands == 'screenshot':
        screenshot = pg.screenshot()
        screenshot.save('screenshot.png')
    elif commands == 'photo':
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        cv2.imwrite('photo.png', frame)  
        cam.release()
    elif commands == 'youtube':
        os.system('start https://www.youtube.com/')
    elif commands == 'exit':
        exit()