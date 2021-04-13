# Importar Biblioteca
from PySimpleGUI import PySimpleGUI as sg
from selenium import webdriver
import time
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#Layout
sg.theme('DarkGreen5') #tema da interface gráfica
layout = [
    [sg.Text('Digite o Texto '),sg.Input()],
    [sg.Button('Enviar!')]
]
#Janela
janela = sg.Window('Linha de Transmissão', layout)

# leitura
butao, mensagem = janela.read()

# Ir até o Wpp Web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(25) #o tempo para abrir a guia do Chrome e digitalizar o código

# Selecionar contatos
contatos = ['Contato 1', 'Contato 2'] #nome exato ao salvo no contato

# Selecionar foto
foto = 'adicionar caminho da imagem que queira enviar'

#Seleçao de quadros
# Pesquisar contatos
def buscar_contato(contato):
   pesquisa_contato =  driver.find_element_by_xpath(
    '//div[contains(@class,"copyable-text selectable-text")]')
   time.sleep (2)
   pesquisa_contato.click()
   pesquisa_contato.send_keys(contato)
   pesquisa_contato.send_keys(Keys.ENTER) #entra na conversa

# Selecionar fotos
def enviar_imagem(foto):
    botao_anexo = driver.find_element_by_css_selector("span[data-testid='clip']")
    botao_anexo.click()
    time.sleep(1)
    localizar_foto = driver.find_element_by_css_selector("input[type='file']")
    localizar_foto.send_keys(foto) #envia a foto
    time.sleep(4)

# Campo de digitação
def enviar_mensagem(mensagem):
    escrever_mensagem =  driver.find_elements_by_xpath(
    '//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    escrever_mensagem[0].send_keys(mensagem)
    escrever_mensagem[0].send_keys(Keys.ENTER) #envia a mensagem
    time.sleep(1)

# Execução
for contato in contatos:
    buscar_contato(contato)
    enviar_imagem(foto)
    enviar_mensagem(mensagem)
    time.sleep(4)