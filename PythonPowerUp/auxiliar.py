"""
    Arquivo que auxilia encontrar a posição certa do mouse, mostrando-a no terminal em 5 segundos
"""

import time
import pyautogui

time.sleep(5)
print(pyautogui.position())

pyautogui.scroll(200)
