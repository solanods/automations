import pandas as pd
import pyautogui as pag
import time

#guias em que o bot vai atuar
url = 'https://webp.caixa.gov.br/portal/consulta/proponente_nv.asp'
planilha = 'https://docs.google.com/spreadsheets/d/1WNtIoLx7IayTJlExcfFLDkSqGYJAjUVIJAdMnCTsOIY/edit#gid=0'

cpf_list = ['81837178020', '00736604006', '05651858458','04601119499', '04488010431', '71411909453', '70312100116', '70064540189', '04941317130', '49579843449']


pag.alert('ATENÇÃO!!! Não faça nenhuma ação em seu computador enquanto o código estiver rodando')
pag.PAUSE = 1
#clicar no ícone do Chrome
pag.moveTo(36, 1047)
pag.click()
pag.write(url)
pag.press('enter')
time.sleep(1)
pag.hotkey('ctrl', 't')
pag.write(planilha)
pag.press('enter')
pag.hotkey('ctrl', '1')

contador = 1
linha = 1
for cpf in cpf_list:
    for digit in cpf:
        pag.write(digit)
    linha = contador + linha
    pag.press('enter') #buscar
    time.sleep(2)
    pag.click(704, 748)
    pag.dragTo(1044, 854, button='left')# select text
    pag.hotkey('ctrl', 'c')# copy text
    pag.hotkey('ctrl', '2')
    time.sleep(1)
    pag.click(2291, 79, clicks=3, interval=0.2)# triple click on the search bar 
    pag.hotkey('ctrl', 'v')
    time.sleep(1)
    pag.click(2291, 79, clicks=3, interval=0.2)# triple click on the search bar
    pag.hotkey('ctrl','c')
    pag.click(1994, 160)#click empity area
    pag.hotkey('ctrl','j')#select name box
    pag.write('A{}'.format(linha)) #write cell
    time.sleep(1)
    pag.press('enter')
    pag.hotkey('ctrl','v')#copy text
    pag.press('tab')
    pag.write('=now()')# insert time
    pag.press('enter')
    pag.hotkey('ctrl', '1')
    pag.click(783, 545)# new search

pag.alert('PROGRAMA FINALIZADO')





