"""
Passo a Passo do projeto:
Passo 1: Entrar no sistema da empresa:
    1. abrir o navegador (chrome)
    2. entrar no site

Passo 2: fazer login

Passo 3: Importar a base de dados

Passo 4: Cadastrar 1 produto

Passo 5: Repetir o processo de cadastro até acabar a base de dados
"""
import pyautogui
import time

pyautogui.PAUSE = 1 

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

LINK = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(LINK)
pyautogui.press("enter")

# Pausa para carregamento do site
time.sleep(3)
pyautogui.click(x=-1240, y=379)
