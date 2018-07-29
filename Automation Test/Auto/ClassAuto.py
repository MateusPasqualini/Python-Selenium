from object import Validation
from object import classPeople
from object import FindElements
from selenium.webdriver.support.ui import Select


class Auto:

    # Construtora da classe auto
    def __init__(self, driver):
        self.elements = FindElements.FindElements(driver)
        self.validacao = Validation.Validation(driver)
        self.pessoa = classPeople.Person()

    # Método para adicionar produto no carrinho
    def add_to_cart(self):
        self.elements.get_image_element().click()
        self.elements.get_add_cart_button().click()
        self.validacao.test_validate_all("Product successfully added to your shopping cart", self.elements.added_in_cart())   # método da classe Validation para validar se o produto foi inserido no carrinho
        self.elements.get_proceder_button().click()
        self.elements.get_checkout_button().click()

    # Método para preencher o campo de email e prosseguir
    def register_email(self):
        self.elements.get_email_field().send_keys(self.pessoa.email)
        self.elements.get_cadastro_button().click()

    # Método para preencher o formulário de cadastro
    def account_filler(self):
        self.elements.get_gender_button().click()
        self.elements.get_first_name_field().send_keys(self.pessoa.nome)
        self.elements.get_last_name_field().send_keys(self.pessoa.last)
        self.elements.get_password_field().send_keys(self.pessoa.senha)
        Select(self.elements.get_day_element()).select_by_value(self.pessoa.dia)
        Select(self.elements.get_month_element()).select_by_value(self.pessoa.mes)
        Select(self.elements.get_year_element()).select_by_value(self.pessoa.ano)
        self.elements.get_address_field().send_keys(self.pessoa.endereco)
        self.elements.get_city_field().send_keys(self.pessoa.cidade)
        Select(self.elements.get_state_box()).select_by_value(self.pessoa.estado)
        self.elements.get_postal_field().send_keys(self.pessoa.postal)
        self.elements.get_cell_field().send_keys(self.pessoa.celular)
        self.elements.get_register_button().click()

    # Método para validar o endereço e prosseguir
    def address_proceed(self):
        self.validacao.test_validate_all(self.pessoa.endereco, self.elements.validate_address())  # método da classe validation para validar se o endereço está correto
        self.elements.get_send_button().click()

    # Método para aceitar os termos
    def accept_terms(self):
        self.elements.get_terms_button().click()
        self.elements.get_proceder2_button().click()

    def finish_buying(self):
        self.validacao.test_validate_all("$18.51", self.elements.validate_price())
        self.elements.get_payment_button().click()
        self.elements.get_buy_button().click()
        self.validacao.test_validate_all("Your order on My Store is complete.", self.elements.validate_purchase())
