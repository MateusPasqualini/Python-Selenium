from object import classPeople
from object import FindElements
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Firefox()  #acessa o webdriver do firefox
driver.get("http://automationpractice.com/index.php")
wait = WebDriverWait(driver, 10)
assert "My Store" in driver.title

#instancniando objeto da classe Person
P1 = classPeople.Person()
#instanciando objeto da classe FindElement
F1 = FindElements.FindElements(driver)

# escolhe o produto pela imagem, encontrando o elemento e clicando
# image = driver.find_element(By.CSS_SELECTOR, "#homefeatured > li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)")
# image.click()
# print(driver.title)

F1.getImageElement().click()
print("OK")

#  Encontra o elemento para adicionar a compra e clica no elemento
# addCart = driver.find_element(By.CSS_SELECTOR, "button.exclusive")
# addCart.click()

F1.getAddCartButton().click()
print("OK")

# Valida se o produto é o escolhido Faded Short Sleeve T-shirts
product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".layer_cart_product > h2:nth-child(2)"))).text
print(product)
assert "Product successfully added to your shopping cart" in product



# Espera e econtra o elemento para proceder para o checkout
# proceed = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a/span"))) #como a página não atualiza é necessário esperar o elemento aparecer e ser clicável
# proceed.click()
F1.getProcederButton().click()
print("OK")

# Procura o elemento do checkout e clica no elemento
# checkout = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]/span")
# checkout.click()

F1.getCheckoutButton().click()
print("OK")

#------------------------------------------------------------------------------------------------------------------

# Procura o elemento do email, insere um endereço de email e procede para cadastro
# email = driver.find_element(By.ID, "email_create")
# email.send_keys(P1.email)
F1.getEmailField().send_keys(P1.email)
print("OK")

# cadastro = driver.find_element(By.NAME, "SubmitCreate")
# cadastro.click()
F1.getCadastroButton().click()
print("OK")

#------------------------------------------------------------------------------------------------------------------

# cadastro
# Espera e encontra o elemento para selecionar o genero
# gender = wait.until(EC.element_to_be_clickable((By.ID, "id_gender1"))) #Foi escolhido o genero masculino
# gender.click()
F1.getGenderButton().click()
print("OK")

# Encontra o elemento para inserir o primeiro nome e insere uma string
# first = driver.find_element(By.ID, "customer_firstname")
# first.send_keys(P1.nome)
F1.getFirstNameField().send_keys(P1.nome)
print("OK")

# encontra o elemento para inserir o sobrenome e insere uma string
# last = driver.find_element(By.ID, "customer_lastname")
# last.send_keys(P1.last)
F1.getLastNameField().send_keys(P1.last)
print("OK")

# encontra o elemento para inserir a senha e insere uma string
# senha = driver.find_element(By.ID, "passwd")
# senha.send_keys("123456")
F1.getPasswordField().send_keys("123456")

print("OK")

# encontra os elementos para definir a data de nascimento e escolhe uma data
# day =driver.find_element(By.ID, "days")
# Select(day).select_by_value(P1.dia)
Select(F1.getDayElement()).select_by_value(P1.dia)
print("OK")

# month = driver.find_element(By.ID, "months")
# Select(month).select_by_value(P1.mes)
Select(F1.getMonthElement()).select_by_value(P1.mes)
print("OK")

# year = driver.find_element(By.ID,"years")
# Select(year).select_by_value(P1.ano)
Select(F1.getYearElement()).select_by_value(P1.ano)
print("OK")

# encontra os elementos para definir o endereço e insere strings
# street = driver.find_element(By.ID, "address1")
# street.send_keys(P1.endereco)
F1.getEnderecoField().send_keys(P1.endereco)
print("OK")

# city = driver.find_element(By.ID,"city")
# city.send_keys(P1.cidade)
F1.getCityField().send_keys(P1.cidade)
print("OK")

# state = Select(driver.find_element(By.ID, "id_state"))
# state.select_by_value(P1.estado)
Select(F1.getStateBox()).select_by_value(P1.estado)
print("OK")

# encontra o elemento de codigo postal e insere uma string
# code = driver.find_element(By.ID,"postcode")
# code.send_keys(P1.postal)
F1.getPostalField().send_keys(P1.postal)
print("OK")

#encontra o elemento de numero de celular e insere uma string
# cell = driver.find_element(By.ID, "phone_mobile")
# cell.send_keys(P1.celular)
F1.getCellField().send_keys(P1.celular)
print("OK")

# encontra o elemento para terminar o cadastro
# account = driver.find_element(By.ID, "submitAccount")
# account.click()
F1.getRegisterButton().click()
print("OK")

#------------------------------------------------------------------------------------------------------------------

#valida endereço
endereco = driver.find_element(By.CSS_SELECTOR, "#address_delivery > li:nth-child(3)").text
print(endereco)
assert P1.endereco in endereco

#encontra o elemento para proceder
# send = driver.find_element(By.NAME, "processAddress")
# send.click()
F1.getSendButton().click()
print("OK")

#------------------------------------------------------------------------------------------------------------------

# encontra o elemento para aceitar os termos e checa
# terms = driver.find_element(By.NAME, "cgv")
# terms.click()
F1.getTermsButton().click()

# encontra o elemento para proceder
# send = driver.find_element(By.NAME, "processCarrier")
# send.click()
F1.getProceder2Button().click()
print("OK")

#------------------------------------------------------------------------------------------------------------------

#valida preço total
price = driver.find_element(By.CSS_SELECTOR, "#total_price").text
print(price)
assert "$18.51" in price


# pagamento
# pay = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div[3]/div[1]/div/p/a")
# pay.click()
F1.getPaymentButton().click()
print("OK")

# finaliza a compra
# buy = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/form/p/button")
# buy.click()
F1.getBuyButton().click()
print("OK")
#------------------------------------------------------------------------------------------------------------------
driver.close()