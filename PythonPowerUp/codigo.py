"""
Passo a Passo do projeto:
Passo 1: Entrar no sistema da empresa:
    1. Abrir o navegador (chrome)
    2. Entrar no site

Passo 2: fazer login
    1. Escrever:
        a. E-mail
        b. Senha
    2. Clicar no botão de Logar

Passo 3: Importar a base de dados

Passo 4: Cadastrar 1 produto
    1. Clicar no 1° campo
    2. Manipular dados do produto:
        a. Código
        b. Marca
        c. Tipo
        d. Categoria
        e. Preço
        f. Custo
        g. Obs
    3. Enviar informações do produto

Passo 5: Repetir o processo de cadastro até acabar a base de dados
"""
import time
import pyautogui
import pandas

pyautogui.PAUSE = 1.2

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

# Passo 2: 1a/2
pyautogui.click(x=-1240, y=379)
pyautogui.write("pythonimpressionador@gmail.com")

# Passo 2: 1b/2
pyautogui.press("tab")
pyautogui.write("sua senha aqui")

# Passo 2: 2/2
pyautogui.click(x=-979, y=532)
time.sleep(3)

# Passo 3:
tabela = pandas.read_csv(r"PythonPowerUp\produtos.csv")

# Passo 4:
for linha in tabela.index:

    # Passo 4: 1/3
    pyautogui.click(x=-1095, y=264)

    # Passo 4: 2a/3
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    # Passo 4: 2b/3
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # Passo 4: 2c/3
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # Passo 4: 2d/3
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # Passo 4: 2e/3
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # Passo 4: 2f/3
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Passo 4: 2g/3
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    # Passo 4: 3/3
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    # Passo 5 -> laço "for"
