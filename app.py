import os
from sys import platform
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

'''
    Get driver selenium!!!!!!
'''
def get_drive():
    headless = False

    if os.getcwd() == '/app': # docker !!!!
        driver_path = os.getcwd()+ "/chromedriver/linux-docker/chromedriver"
        headless = True
    else:
        if platform == "linux" or platform == "linux2":
            driver_path = os.getcwd() + "/chromedriver/linux/chromedriver"
        elif platform == "darwin": #mac
            driver_path = os.getcwd() + "/chromedriver/mac/chromedriver"
    #print(f"DRIVER: {driver_path}")
    options = webdriver.ChromeOptions()

    # diretorio padrao sem popup!!!!
    prefs = {
        "profile.default_content_settings.popups": 0, 
        "download.default_directory": os.getcwd() + "/tmp", 
        "directory_upgrade": True
    }

    options.add_experimental_option("prefs", prefs)
    #options.add_argument('--no-sandbox') # necessário para rodar nesta versao do chromedriver
    options.add_argument('--disable-dev-shm-usage') # para nao falahar em paginas muito grandes
    options.add_argument('--ignore-certificate-errors') # ignorar erro de certificado
    options.add_argument("--lang=pt-BR") # definição de linguagem
    # no screens
    if headless == True:
        options.add_argument('--headless') # sem exibir uma tela
    options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    driver = webdriver.Chrome( executable_path=driver_path, options=options)

    return driver
driver = get_drive()
# definir um padrao de 10s para qq wait
wait = WebDriverWait(driver, 10)

driver.get("https://www.google.com.br")
xpath = "//input[@title='Pesquisar']"


search = "https://twitter.com/escovadordebit"


wait.until(EC.presence_of_element_located((By.XPATH, xpath))).send_keys("Escovador de bit")

wait.until(EC.presence_of_element_located((By.XPATH, xpath))).send_keys(Keys.ENTER)

xpath = f'//a[@href="{search}"]/h3'
print(wait.until(EC.presence_of_element_located((By.XPATH, xpath))).text)

