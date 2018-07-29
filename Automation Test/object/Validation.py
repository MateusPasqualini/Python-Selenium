class Validation:

    # Construtora da classe Validation
    def __init__(self, driver):
        self.driver = driver

    # Método para validações
    def test_validate_all(self, value, driver):
        self.test_validation(value, driver)

    # Método com assert para validar dois valores
    def test_validation(self, value, assert_value):
        assert value == assert_value
