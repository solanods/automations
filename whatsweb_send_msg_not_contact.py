from selenium import webdriver  #pip install selenium
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
import time
import pyautogui as pag
import pyperclip

pag.PAUSE=2
#Abre o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') #abre o site Whatsapp Web
driver.maximize_window()
time.sleep(15) #da um sleep de 15 segundos, tempo para scannear o QRCODE






#Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida */* )
midia = "/home/sol/Imagens/ibiza_capa.jpg"

#url_base
url_base = 'https://api.whatsapp.com/send?phone=55'
#contacts
contacts = ['51993030835', '51991359313', '51996802979']

#Funcao que envia midia como mensagem
def enviar_midia(midia):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(midia)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()

pag.click(2374, 78, clicks=3)
pag.write('https://api.whatsapp.com/send?phone=5551991359313')
pag.press('enter')
pag.click(1001, 199)
pag.click(1502, 260)

for contact in contacts:
    pag.PAUSE=3
    # Mensagem - Mensagem que sera enviada
    mensagem = 'Olá, meu nome é Roselaine Costa. Sou correspondente da Caixa e estou aqui para atender sua solicitação sobre empreendimentos em Novo Hamburgo. Esse é o mais novo  lançamento da modalidade Casa Verde Amarela.\nResponda SIM para mais informações.'

    pag.click(2374, 78, clicks=3)
    pag.write(url_base.lower() + contact.lower())
    pag.press('enter')
    pag.click(1266, 404)#iniciar conversa
    pag.click(1270, 479)#use o whats web
    #pyperclip.copy(mensagem)
    #pag.click(1141, 960, clicks=2)#barra de msg
    #pag.hotkey('ctrl', 'v')
    #pag.press('enter')
    enviar_midia(midia)
    pyperclip.copy(mensagem)
    pag.click(1141, 960)#barra de msg
    pag.hotkey('ctrl', 'v')
    pag.press('enter')


