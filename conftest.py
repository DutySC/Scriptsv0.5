import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

p_link = "http://172.17.0.2:4444/wd/hub" # адрес для инициализации драйвера
def browser_SNILS():
    service = Service(executable_path="./chromedriver.exe") # путь до драйвера
    chrome_options = ChromeOptions() # объект для опций
    chrome_options.add_argument('--headless') # фоновый режим
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) # включение экспериментальных функций
    chrome_options.add_argument('--ignore-certificate-errors') # игнорирование проверки сертификата
    chrome_options.add_argument('--ignore-ssl-errors') # игнорирование проверки сертификата
    chrome_options.add_argument('--start-maximized')  # полный экран
    driver = webdriver.Chrome(service=service, options=chrome_options) # настройка драйвера
    link_1 = 'https://ortex.github.io/snils-generator/' # адрес для подключения
    driver.get(link_1) # подключение по указанному адресу
    snils_1 = driver.find_element(By.XPATH, '//span').text # получаем содержимое элемента
    snils_2 = snils_1.replace(" ", "") # убираем пустые символы (пробелы) в полученном значении
    return snils_2 # получаем значение сгенерированного СНИЛСа

@pytest.fixture(scope='function')
def browser_PK():
    # service = Service(executable_path="chromedriver.exe") # путь до драйвера
    chrome_options = ChromeOptions() # объект для опций
    chrome_options.add_argument('--headless') # фоновый режим
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) # включение экспериментальных функций
    chrome_options.add_argument('--ignore-certificate-errors') # игнорирование проверки сертификата
    chrome_options.add_argument('--ignore-ssl-errors') # игнорирование проверки сертификата
    chrome_options.add_argument('--start-maximized')  # полный экран
    driver = webdriver.Remote(command_executor=f'{p_link}', options=chrome_options)  # настройка драйвера
    # driver = webdriver.Remote(f"{p_link}", DesiredCapabilities.CHROME, options=chrome_options)  # настройка драйвера
    # driver = webdriver.Chrome(service=service, options=chrome_options) # настройка драйвера
    link_1 = 'https://192.168.233.171:25443/' # адрес для подключения
    link_2 = 'http://192.168.234.31:1580/'  # адрес для подключения
    driver.get(link_2) # подключение по указанному адресу
    yield driver # возврат из функции с сохранением состояния ее переменных
    driver.quit() # выход из браузера

@pytest.fixture(scope='function')
def browser_RSO():
    service = Service(executable_path="./chromedriver.exe") # путь до драйвера
    chrome_options = ChromeOptions() # объект для опций
    # chrome_options.add_argument('--headless') # фоновый режим
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) # включение экспериментальных функций
    chrome_options.add_argument('--ignore-certificate-errors') # игнорирование проверки сертификата
    chrome_options.add_argument('--ignore-ssl-errors') # игнорирование проверки сертификата
    chrome_options.add_argument('--start-maximized')  # полный экран
    driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options) # настройка драйвера
    link_1 = 'http://192.168.234.31:1580/' # адрес для подключения
    driver.get(link_1) # подключение по указанному адресу
    yield driver # возврат из функции с сохранением состояния ее переменных
    driver.quit()  # выход из браузера

@pytest.fixture(scope='function')
def browser_NSO():
    service = Service(executable_path="./chromedriver.exe") # путь до драйвера
    chrome_options = ChromeOptions() # объект для опций
    # chrome_options.add_argument('--headless') # фоновый режим
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) # включение экспериментальных функций
    chrome_options.add_argument('--ignore-certificate-errors') # игнорирование проверки сертификата
    chrome_options.add_argument('--ignore-ssl-errors') # игнорирование проверки сертификата
    chrome_options.add_argument('--start-maximized')  # полный экран
    driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options) # настройка драйвера
    link_1 = 'http://192.168.233.169:3980/' # адрес для подключения
    driver.get(link_1) # подключение по указанному адресу
    yield driver # возврат из функции с сохранением состояния ее переменных
    driver.quit()  # выход из браузера

@pytest.fixture(scope='function')
def browser_KURO():
    service = Service(executable_path="./chromedriver.exe") # путь до драйвера
    chrome_options = ChromeOptions() # объект для опций
    # chrome_options.add_argument('--headless') # фоновый режим
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) # включение экспериментальных функций
    chrome_options.add_argument('--ignore-certificate-errors') # игнорирование проверки сертификата
    chrome_options.add_argument('--ignore-ssl-errors') # игнорирование проверки сертификата
    chrome_options.add_argument('--start-maximized')  # полный экран
    driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options) # настройка драйвера
    link_1 = 'http://192.168.234.14:7280/' # адрес для подключения
    driver.get(link_1) # подключение по указанному адресу
    yield driver # возврат из функции с сохранением состояния ее переменных
    driver.quit()  # выход из браузера
