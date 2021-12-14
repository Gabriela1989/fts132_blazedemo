from selenium import webdriver

# Início
def before_all(context):
    # Declaração do selenium, instanciar como o navegador e apontar o driver
    context.driver = webdriver.Chrome('drivers/chrome/96/chromedriver.exe')

    context.driver.maximize_window()

# Fim
def after_all(context):
    # Desligar /  Destruir o objeto Selenium
    context.driver.quit()

    print('Passo Z - Depois de tudo')

# Bloco executado ao final de cada step
# def after_step(context, step):
# print()