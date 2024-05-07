from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests import config


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def acessar(self, url):
        return self.driver.get(url)
    # config para saucelabs

    # def acessar(self, url):  # melhorado
    #     if url.startwith('http'):  # o endereçp começa com http (ou https)
    #         self.driver.get(url)
    #     else:
    #         self.driver.get(config.baseurl + url)
    #
    #         # imagine que o endereço viesse como '/login'
    #         # Endereço base +/login
    #         # https://the-internet.herokuapp.com/login

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def escrever(self, locator, texto):
        return self.encontrar_elemento(locator).send_keys(texto)

    def clicar(self, locator):
        return self.encontrar_elemento(locator).click()

    def verificar_elemento_existe(self, locator):
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).is_displayed()

    def pegar_texto_elemento(self, locator):
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).text

    def esperar_elemento_aparecer(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
