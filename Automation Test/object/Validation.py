from object import classPeople
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Validation:

    # Construtora da classe Validation
    def __init__(self, driver):
        self.driver = driver
        self.P1 = classPeople.Person()
        self.wait = WebDriverWait(self.driver, 10)
        self.product = ''
        self.adress = ''
        self.price = ''

    # Método para validar o produto escolhido
    def validate_product(self):
        self.product = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".layer_cart_product > h2:nth-child(2)"))).text
        assert "Product successfully added to your shopping cart" in self.product

    # Método para validar o endereço da pessoa
    def validate_address(self):
        self.address = self.driver.find_element(By.CSS_SELECTOR, "#address_delivery > li:nth-child(3)").text
        assert self.P1.endereco in self.address

    # Método para valida o preço final da compra
    def validate_price(self):
        self.price = self.driver.find_element(By.CSS_SELECTOR, "#total_price").text
        assert "$18.51" in self.price
