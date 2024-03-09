"""
Passo a passo:
    Passo 1: Importar a framework do site

    Passo 2: função principal, criando:
        1. O site
        2. Bate-papo
            1. Criando o campo de mensagem
            2. Enviando a mensagem

        3. Tela inicial do site
            1. Boas-vindas e selecionar nome do usúario
            2. Criando o modal
            3. Adicionando o botão inicial e o nome da página

    Passo 3: Cria o app chamando a função principal
"""
# Passo 1:
import flet as ft

# Passo 2:
def main(pagina):
    """
    Função principal que cria o site
    :param pagina: página informada
    """
    # Passo 2: 1/3
    texto = ft.Text("Hashzap")

    # Passo 2: 2/3
    chat = ft.Column() # Criar tunel de comunicação: Dizer ao programa que quer criá-lo; 


    def enviar_mensagem_tunel(mensagem):
        # Adicione a mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(event):
        print("Enviar mensagem")
        # envie a mensagem ao chat
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        # limpe o campo mensagem
        campo_mensagem.value = ""
        pagina.update()


    # Passo 2: etapa 2/3: 1/2
    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)

    # Passo 2: etapa 2/3: 2/2
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_enviar = ft.Row([campo_mensagem, botao_enviar]) # Linha = Row

    def entrar_chat(event):
        print("Entrar chat")
        # Fechar popup
        popup.open = False
        # Tirar o botão iniciar chat
        pagina.remove(botao_iniciar)
        # Tirar o título hashzap
        pagina.remove(texto)
        # Criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        # Colocar o campo de digitar mensagem
        # Criar o botão de enviar
        pagina.add(linha_enviar)
        pagina.update()

    # Passo 3/3: 1/3
    titulo_popup = ft.Text("Bem-vindo ao Hashzap")

    nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    # Passo 3/3: 2/3
    popup = ft.AlertDialog(open=False, modal=True,
                           title=titulo_popup,
                           content=nome_usuario,
                           actions=[botao_entrar])


    def open_popup(event):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    # Passo 3/3: 3/3
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=open_popup)
    pagina.add(botao_iniciar)
    pagina.add(texto)


# Passo 3:
ft.app(target=main, view=ft.WEB_BROWSER)
