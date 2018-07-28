from selenium import webdriver
from Auto import ClassAuto


# acessa o webdriver do firefox
driver = webdriver.Firefox()

# Acessa o site automation practice
driver.get("http://automationpractice.com/index.php")

# Instacia um objeto para classe Auto para rodar o programa
auto = ClassAuto.Auto(driver)

# Roda o método para adicionar os produtos ao carrinho
# e prosseguir (Também valida se o produto foi adicionado ao carrinho)
auto.add_to_cart()

# Roda o método para registrar o email e prossegue
auto.register_email()

# Roda o método para preencher o formulário de cadastro
auto.account_filler()

# Roda o método que valida o endereço e prossegue
auto.address_proceed()

# Roda o método que checa a caixa de termos e serviços
auto.accept_terms()

# Roda o método que termina a compra (Também valida se o valor final está correto)
auto.finish_buying()

# Fecha o navegador
driver.close()
