"""This is a simple bot that take a rent list from https://www.proprietariodireto.com.br and send a message for each owner"""


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#================================GET THE LINKS===============================================================
ads_links = []
for i in range(1, 5):
    driver.get(f"https://www.proprietariodireto.com.br/aluguel/imovel/direto-com-proprietario?page={i}")
    time.sleep(5)
    links = driver.find_elements(By.TAG_NAME, 'a')
    for link in links:
        ads_links.append(link.get_attribute('href'))

#================================CLEAN THE LINKS==============================================================

# Remove none objects
ads_links = [link for link in ads_links if isinstance(link, str)]

# Get the ads pattern with a regex
ads_links = [link for link in ads_links if re.search('.+\d{18}', link)]

# Get the unique objects
ads_links = list(set(ads_links))

# Filter by substring 'https://www.proprietariodireto.com.br/alugar'
rent_ads = [link for link in ads_links if 'https://www.proprietariodireto.com.br/alugar' in link]


#================================LOGIN IN THE PAGE============================================================
USERNAME = 'youremail@email.com'
PASSWORD = '999999999'
driver.get('https://www.proprietariodireto.com.br/')
time.sleep(5)
driver.maximize_window()
driver.find_element(By.XPATH, '/html/body/header/div/div/div[2]/div/a').click()#entrar
driver.find_element(By.XPATH,'//*[@id="signIn"]/div[1]/div/input').send_keys(USERNAME)
driver.find_element(By.XPATH,'//*[@id="signIn"]/div[2]/div/input').send_keys(PASSWORD)
driver.find_element(By.XPATH,'//*[@id="signIn"]/div[3]/button').click()
time.sleep(5)

#================================SEND MESSAGES============================================================
msg = """IMÓVEL PARADO?   FALE COMIGO!\nAgora você pode anunciar ou alugar imóveis na plataforma que nasceu para simplificar o processo de locação do início ao fim.\n
VEJA OS BENEFÍCIOS DE ALUGAR PELO QUINTO ANDAR\n
* Um imóvel alugado a cada oito minutos.\n
* Receba em dia, independente do pagamento do inquilino.\n
* Anúncio online, gratuito e com fotos profissionais.\n
* Imóvel com proteção de até R$ 50 mil contra danos.\n

Utilize meu link na hora de se cadastrar e ganhe R$ 200 de desconto.\n

http://quin.to/drhpia?codigo=BOMb0Y \n

Ou entre em contato enviando seu nome completo, telefone e endereço do imóvel que realizo o cadastro para você.\n
Tenha um ótimo dia!

"""

for link in rent_ads[:4]:
    driver.get(link)
    driver.maximize_window()
    time.sleep(5)
    env_msg = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[1]/div/div[4]/div[2]/div/button')
    env_msg.click()
    time.sleep(2)
    text_area = driver.find_element(By.XPATH, '//*[@id="send-message-text"]')
    text_area.send_keys(msg)
    numbers = driver.find_element(By.XPATH, '//*[@id="sendMessage"]/div/div/div[2]/div/div')#captcha the numbers
    values = numbers.text #string transform
    values = values.split()#split the elements
    result = int(values[0]) + int(values[1])#transform and sum
    result_field = driver.find_element(By.XPATH, '//*[@id="churrumino"]')
    result_field.send_keys(str(result))
    driver.find_element(By.XPATH, '//*[@id="sendMessage"]/div/div/div[3]/button').click()
    time.sleep(3)

driver.close()








