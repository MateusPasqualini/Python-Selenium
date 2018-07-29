from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FindElements:

    # construtora da classe FindElements que recebe como parâmetro um objeto WebDriver
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Método que retorna o elemento da Imagem do produto
    def get_image_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#homefeatured > li:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)")

    # Método que retorna o elemento do botão para adicionar ao carrinho
    def get_add_cart_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button.exclusive")

    # Método que retorna o elemento para proceder
    def get_proceder_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a/span"))) #como a página não atualiza é necessário esperar o elemento aparecer e ser clicável

    # Método que retornar uma string de um elemento
    def added_in_cart(self):
       return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".layer_cart_product > h2:nth-child(2)"))).text

    # Método que retorna o elemento para checkout
    def get_checkout_button(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]/span")

    # Método que retorna o elemento para o campo do Email
    def get_email_field(self):
        return self.driver.find_element(By.ID, "email_create")

    # Método que retorna o elemento para o botão de cadastro
    def get_cadastro_button(self):
        return self.driver.find_element(By.NAME, "SubmitCreate")

    # Método que retorna o elemento para o botão masculino
    def get_gender_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "id_gender1")))

    # Método que retorna o elemento para o campo do primeiro nome
    def get_first_name_field(self):
        return self.driver.find_element(By.ID, "customer_firstname")

    # Método que retorna o elemento para o campo do sobrenome
    def get_last_name_field(self):
        return self.driver.find_element(By.ID, "customer_lastname")

    # Método que retorna o elemento para o campo da senha
    def get_password_field(self):
        return self.driver.find_element(By.ID, "passwd")

    # Método que retorna o elemento para a caixa dos dias
    def get_day_element(self):
        return self.driver.find_element(By.ID, "days")

    # Método que retorna o elemento para caixa dos meses
    def get_month_element(self):
        return self.driver.find_element(By.ID, "months")

    # Método que retorna o elemento para caixa do anos
    def get_year_element(self):
        return self.driver.find_element(By.ID, "years")

    # Método que retorna o elemento para o campo de endereço
    def get_address_field(self):
        return self.driver.find_element(By.ID, "address1")

    # Método que retorna o elemento para o campo da cidade
    def get_city_field(self):
        return self.driver.find_element(By.ID, "city")

    # Método que retorna o elemento para a caixa de estados
    def get_state_box(self):
        return self.driver.find_element(By.ID, "id_state")

    # Método que retorna o elemento para o campo de codigo postal
    def get_postal_field(self):
        return self.driver.find_element(By.ID, "postcode")

    # Método que retorna o elemento para o campo de celular
    def get_cell_field(self):
        return self.driver.find_element(By.ID, "phone_mobile")

    # Método que retorna o elemento para o botão de registrar
    def get_register_button(self):
        return self.driver.find_element(By.ID, "submitAccount")

    # Método que retorna um string de um elemento
    def validate_address(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#address_delivery > li:nth-child(3)").text

    # Método que retorna o elemento para o botão de proceder
    def get_send_button(self):
        return self.driver.find_element(By.NAME, "processAddress")

    # Método que retorna o elemento para o botão de aceitar os termos
    def get_terms_button(self):
        return self.driver.find_element(By.NAME, "cgv")

    # Método que retorna o elemento para o botão de proceder
    def get_proceder2_button(self):
        return self.driver.find_element(By.NAME, "processCarrier")

    # Método que retorna uma string de um elemento
    def validate_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#total_price").text

    # Método que retorna o elemento para o botão de pagamento
    def get_payment_button(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div[3]/div[1]/div/p/a")

    # Método que retorna o elemento para o botão de compra
    def get_buy_button(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/form/p/button")
    # Método que retorna uma string de um elemento
    def validate_purchase(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".cheque-indent > strong:nth-child(1)").text
