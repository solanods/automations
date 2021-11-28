import pyautogui
import time

perfil_alvo = 'vidasimples'

pyautogui.alert('ATENÇÃO!!! Não faça nenhuma ação em seu computador enquanto o código estiver rodando')
pyautogui.PAUSE = 1.5
#clicar no ícone do Chrome
pyautogui.moveTo(x=36, y=1047)
pyautogui.click()
time.sleep(3)
pyautogui.write('instagram')
pyautogui.press('enter')
time.sleep(5)
# barra de pesquisa
pyautogui.moveTo(x=1242, y=159)
pyautogui.click()
pyautogui.write(perfil_alvo)
pyautogui.press(['tab', 'tab', 'enter'])
# seguidores
pyautogui.moveTo(x=1340, y=282)
pyautogui.click()
time.sleep(1.5)
# janela de seguidores
for i in range(7):
    pyautogui.click(1411, 433)
    time.sleep(1.5)
    pyautogui.click(1416, 484)
    time.sleep(1.5)
    pyautogui.click(1413, 530)
    time.sleep(1.5)
    pyautogui.click(1418, 579)
    time.sleep(1.5)
    pyautogui.click(1421, 625)
    time.sleep(1.5)
    pyautogui.click(1419, 670)
    time.sleep(1.5)
    pyautogui.click(1421, 713)
    time.sleep(1.5)
    pyautogui.click(1421, 755)
    time.sleep(1.5)
    #scroll
    pyautogui.mouseDown(1472, 764)
    time.sleep(1.5)
    pyautogui.mouseUp()

#fechar janela seguidores
pyautogui.click(1455, 395)
#fechar chrome
pyautogui.click(2542, 41)
pyautogui.alert('Processo finalizado.')









