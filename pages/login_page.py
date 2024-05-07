from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    username_input = (By.CSS_SELECTOR, 'input#username')  # Localizador do campo de usuário
    password_input = (By.CSS_SELECTOR, 'input#password')  # Localizador do campo de senha
    login_button = (By.CSS_SELECTOR, 'button.radius')  # Localizador do botão de login
    message_success = (By.CSS_SELECTOR, '.success')  # Localizador da mensagem de sucesso
    message_failure = (By.CSS_SELECTOR, 'div.flash.error')  # Localizador da mensagem de erro
    login_form = (By.ID, 'login')

    def __init__(self, driver):
        self.driver = driver
        #   endereço na config.baseurl
        self.acessar('https://the-internet.herokuapp.com/login')  # Navegar para a página de login
        # Validandi se o formulário de login está visível
        assert self.esperar_elemento_aparecer(self.login_form)

    def fazer_login(self, username, password):
        # Preencher o campo de usuário e senha e clicar no botão de login
        self.escrever(self.username_input, username)
        self.escrever(self.password_input, password)
        self.clicar(self.login_button)

    def verificar_mensagem_sucesso(self):
        # Verificar se a mensagem de sucesso está visível na página
        # return self.driver.find_element(*self.message_success).is_displayed()
        return self.verificar_elemento_existe(self.message_success)

    def verificar_mensagem_error(self):
        # Verificar se a mensagem de erro está visível na página
        return self.verificar_elemento_existe(self.message_failure)

    def verificar_mensagem_texto(self, texto_esperado):
        # Verificar se o texto da mensagem de sucesso está correto
        texto_encontrado = self.pegar_texto_elemento(self.message_success)
        return texto_encontrado == texto_esperado

    def verificar_mensagem_texto_invalido(self, texto_esperado):
        # Verificar se o texto da mensagem de erro de usuário inválido está correto
        texto_encontrado = self.pegar_texto_elemento(self.message_failure)
        return texto_encontrado == texto_esperado

    def verificar_mensagem_texto_password_invalido(self, texto_esperado):
        # Verificar se o texto da mensagem de erro de senha inválida está correto
        texto_encontrado = self.pegar_texto_elemento(self.message_failure)
        return texto_encontrado == texto_esperado
