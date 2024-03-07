"""
Passo a Passo do projeto:
Passo 1: Entrar no sistema da empresa:
    1. Abrir o navegador (chrome)
    2. Entrar no site

Passo 2: fazer login
    1. Escrever o e-mail
    2. Escrever a senha
    3. Clicar no botão de Logar

Passo 3: Importar a base de dados

Passo 4: Cadastrar 1 produto

Passo 5: Repetir o processo de cadastro até acabar a base de dados
"""
import time
import pyautogui

pyautogui.PAUSE = 1

# Passo 1: 1/2
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Passo 1: 2/2
LINK = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(LINK)
pyautogui.press("enter")

# Pausa para carregamento do site
time.sleep(3)

# Passo 2: 1/3
pyautogui.click(x=-1240, y=379)
pyautogui.write("pythonimpressionador@gmail.com")

# Passo 2: 2/3
pyautogui.press("tab")
pyautogui.write("sua senha aqui")

# Passo 2: 3/3
pyautogui.click(x=-979, y=532)
time.sleep(3)

# Passo 3:

