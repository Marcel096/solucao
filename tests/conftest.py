import os
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--baseurl',
        action='store',
        default='https://the-internet.herokuapp.com/',
        help='Url base da aplicação alvo do teste'
    )
    parser.addoption(
        '--host',
        action='store',
        default='saucelabs',
        help='Onde vamos executar nossos testes: localhost ou saucelabs'
    )
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='O nome do navegador utilizado nos testes'
    )
    parser.addoption(
        '--browserversion',
        action='store',
        default='120.0',
        help='Versão dp brwoser'
    )
    parser.addoption(
        '--platform',
        action='store',
        default='linux',
        help='Sistema Operacional a ser utilizado durante os testes (apenas no saucelabs'
    )

@pytest.fixture
def driver(request):  # Inicialização do teste
    config.baseurl = request.config.getoptions('--baseurl')
    config.host = request.config.getoptions('--host')
    config.browser = request.config.getoptions('--browser')
    config.browserversion = request.config.getoptions('--browserversion')
    config.platform = request.config.getoptions('--platform')

    if config.host == 'saucelabs':
        test_name = request.node.name
        capabilities = {
            'browserName': config.browser,
            'browserVersion': config.browserversion,
            'platformName': config.platform,
            'sauce:option': {
                'name': test_name
            }
        }
        # _credentials = os.environ['oauth-marcelo.ds9687-98eb8'] + ':' + os.environ['a4de4dd3-00ed-4467-9e89-b35723b5cc4a']
        # _url = 'https://' + _credentials + 'https://@ondemand.us-west-1.saucelabs.com:443/wd/hub'

        _url = 'https://oauth-marcelo.ds9687-98eb8:a4de4dd3-00ed-4467-9e89-b35723b5cc4a@ondemand.us-west-1.saucelabs.com:443/wd/hub'
        driver_ = webdriver.Remote(_url, capabilities)
    else:  # execução local/localhost
        if config.browser == 'chrome':
            path_chromedriver = os.path.join('vendor', 'chromedriver')
            if os.path.isfile(path_chromedriver):
                driver_ = webdriver.Chrome()
            else:
                driver_ = webdriver.Chrome()
        elif config.browser == 'firefox':
            _geckodriver = os.path.join('vendor', 'geckodriver')
            if os.path.isfile(_geckodriver):
                driver_ = webdriver.Firefox()
            else:
                driver_ = webdriver.Firefox()

    def quit():  # Finalização dos tests - similar ao after ou teardown
        # sinalizaçao de passou ou falhou confrome o retorno da requição
        sauce_result = 'failed' if request.node.rep_call.failed else 'passed'
        driver_.execute_script('sauce:job-result={}'.format(sauce_result))
        driver_.quit()

    request.addfinalizer(quit)
    return driver_


@pytest.hookimpl(hookwrapper=True, tryfirst=True) # Implementação do gatilh de comunicação com Saucelabs
def pytest_runtest_makereport(item, call):

    #  parametros para geração do ralatório/ informação dos reesultados
    outcome = yield
    rep = outcome.get_result()

    # definir atributos para relatório
    setattr(item, 'rep' + rep.when, rep)
