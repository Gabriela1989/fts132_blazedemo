from selenium import webdriver

# Início
def before_all(context):
    # Declaração do selenium, instanciar como o navegador e aporntar o driver
    context.driver = webdriver.Chrome('drivers/chrome/96/chromedriver.exe')

    context.driver.maximize_window()

# Fim
def after_all(context):
    # Desligar /  Destruir o objeto Selenium
    context.driver.quit()

    print('Passp Z - Depois de tudo')
