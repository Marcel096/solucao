# from selenium import webdriver  # config sauce
# import os
import pytest

from pages import login_page
from pages.login_page import LoginPage


# Fixture para configurar o driver antes dos testes
@pytest.fixture
def navegador(driver):  # deixou de receber request e recebe driver
    return login_page.LoginPage(driver)


    # config saucelabs do bloco driver, utilizar o return login_page
    # # Caminho para o chromedriver
    # path_chrome_driver = os.path.join('vendor', 'chromedriver')
    #
    # # Verifica se o chromedriver está disponível no sistema
    # if os.path.isfile(path_chrome_driver):
    #     browser = webdriver.Chrome()
    # else:
    #     browser = webdriver.Chrome()

    # Instancia a página de login
    # login_page = LoginPage(browser)

    # # Define a função para fechar o driver ao final dos testes
    # def fechar_driver():
    #     browser.quit()
    #
    # request.addfinalizer(fechar_driver)
    # return login_page


# Teste para login com sucesso
def test_login_com_sucesso(navegador):
    mensagem_texto_esperado = 'You logged into a secure area!\n×'
    navegador.fazer_login('tomsmith', 'SuperSecretPassword!')
    assert navegador.verificar_mensagem_sucesso()
    assert navegador.verificar_mensagem_texto(mensagem_texto_esperado)


# Teste para login inválido
def test_login_invalido(navegador):
    mensagem_texto_esperado = 'Your username is invalid!\n×'
    navegador.fazer_login('dostoievsky', 'SuperSecretPassword!')
    assert navegador.verificar_mensagem_error()
    assert navegador.verificar_mensagem_texto_invalido(mensagem_texto_esperado)


# Teste para senha inválida
def test_password_invalido(navegador):
    mensagem_texto_esperado = 'Your password is invalid!\n×'
    navegador.fazer_login('tomsmith', 'raskolnicov')
    assert navegador.verificar_mensagem_error()
    assert navegador.verificar_mensagem_texto_password_invalido(mensagem_texto_esperado)


# Teste para campo vazio
def test_campo_vazio(navegador):
    mensagem_texto_esperado = 'Your username is invalid!\n×'
    navegador.fazer_login('', '')
    assert navegador.verificar_mensagem_error()
    assert navegador.verificar_mensagem_texto_invalido(mensagem_texto_esperado)


    # old
    # driver.get('https://the-internet.herokuapp.com/login')
    # driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys('tomsmith')
    # driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys('SuperSecretPassword!')
    # driver.find_element(By.CSS_SELECTOR, 'button.radius').click()
    # assert driver.find_element(By.CSS_SELECTOR, '.success').is_displayed()
    # assert driver.find_element(By.CSS_SELECTOR, 'div.flash.success').text == 'You logged into a secure area!\n×'