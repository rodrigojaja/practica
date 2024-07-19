from selenium.webdriver.common.by import By

# Paso 1. Declara la clase de objeto de la página
class LoginPageAround:
    # Paso 2. Define el localizador para el encabezado de Iniciar sesión
    entrance_title = [By.CLASS_NAME, 'auth-form__title']
    # Define el localizador para el encabezado de Registrarse
    registration_header = [By.CLASS_NAME, 'header__auth-link']

    # Paso 3. Agrega el constructor de clase
    def __init__(self, driver):
        self.driver = driver  # Inicializa los atributos

    # Paso 4. Agrega los casos de prueba
    # El método comprueba que el encabezado Iniciar sesión esté presente
    def check_presence_of_entrance_title(self):
        actual_value = self.driver.find_element(*self.entrance_title).text
        expected_value = 'Iniciar sesión'
        assert actual_value == expected_value, f'Valor esperado: "{expected_value}", valor actual: "{actual_value}"'

    # El método comprueba que el encabezado Registrarse esté presente
    def check_presence_of_header_registration(self):
        actual_value = self.driver.find_element(*self.registration_header).text
        expected_value = 'Registrarse'
        assert actual_value == expected_value, f'Valor esperado: "{expected_value}", valor actual: "{actual_value}"'