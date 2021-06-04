from selenium import webdriver

chrome = webdriver.Chrome()
chrome.implicitly_wait(10) # Estabelece um tempo máximo de 10 segundos para cada etapa do programa ser executada

# Vai ao site do Verdemar
chrome.get("https://www.verdemaratevoce.com.br/")

# Fecha o pop up de aviso na tela
chrome.find_element_by_xpath('//*[@id="largeModal"]/div/div/div[3]/button').click()

# Pesquisa "Heineken" no campo de busca
chrome.find_element_by_xpath('//*[@id="inputBuscaRapida"]').send_keys('Heineken')

# Clica no botão de "Busca"
chrome.find_element_by_xpath('/html/body/app-root/app-header/div/div/div/div/div/div[2]/form/button').click()

# Clica na garrafa de 350ml
chrome.find_element_by_xpath('/html/body/app-root/app-produto-busca/div/div/div[1]/div/div[2]/app-produto-card/div/div/app-produto-imagem/a/div/img').click()

# Pega o valor do preço por unidade e mostra no terminal
preco = chrome.find_element_by_class_name('info-price').text
print(f"Preço: {preco}")



