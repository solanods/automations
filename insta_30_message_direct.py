import pyautogui as pag
import pyperclip
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

options = ChromeOptions()
options.headless = False #headless browser
driver = Chrome(executable_path='/home/sol/notebooks/web_scraper_python/chromedriver', options = options)


#login
username = 'solanobikers'
password = 'uantiussu'
driver.get('https://www.instagram.com') #start url
driver.maximize_window()
time.sleep(2)
input_user = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
input_user.send_keys(username)
input_user.click()
input_pass = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
input_pass.send_keys(password)
input_pass.click()
button_entrar = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
button_entrar.click()
time.sleep(4)
agora_nao = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
agora_nao.click()
time.sleep(2)
pag.click(1277, 726)
time.sleep(2)

lista_familia = ['golden.malandrinho', 'roselaine.amaro', 'natalia_19n']
#inicio do loop
for contact in lista_familia:
    pag.PAUSE = 2
    pag.click(1555, 172)  # direct_link
    pag.click(1429, 699)#botao azul enviar mgs
    pag.write(contact)
    pag.press('tab')
    pag.press('enter')
    pag.click(1425, 320)#avançar
    mensagem1 = 'Olá, '
    mensagem2 = contact
    mensagem3 = '. Prometo que tá quase acabando esse teste. Meu nome é Roselaine estou aqui para lhe apresentar uma grande oportunidade.'
    mensagem = mensagem1 + mensagem2 + mensagem3
    pyperclip.copy(mensagem)
    pag.click(1282, 948)#barra de msg
    pag.hotkey('ctrl', 'v')
    pag.press('enter')
    pag.click(1649, 955)  #image_icon
    pag.hotkey('ctrl', 'f')
    pag.write('ibiza_capa')
    pag.press('down')
    pag.press('enter')
    time.sleep(5)









