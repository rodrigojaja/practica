# Clase de importación para encontrar por localizadores
from selenium.webdriver.common.by import By

# Paso 1. Declara la clase de objeto de la página
class LoginPageAround:
    # Paso 2. Define el localizador del campo Correo electrónico
    email_field = [By.ID, 'email']
    # Define el localizador del campo Contraseña
    password_field = [By.ID, 'password']

    # Paso 3. Agrega el constructor de clase
    def __init__(self, driver):
        self.driver = driver  # Inicializa los atributos

    # Paso 4. Agrega interacciones como métodos
    # El método rellena el campo Correo electrónico
    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    # El método rellena el campo Contraseña
    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    # Paso 5. Agrega los casos de prueba
    # El método comprueba Correo electrónico contenga los datos de entrada pasados
    def check_email_value(self, email):
        actual_value = self.driver.find_element(*self.email_field).get_property("value")
        expected_value = email
        assert actual_value == expected_value, f'Valor esperado de Correo electrónico: "{expected_value}", valor actual: "{actual_value}"'

    # El método comprueba que Contraseña contenga los datos de entrada pasados
    def check_password_value(self, password):
        actual_value = self.driver.find_element(*self.password_field).get_property("value")
        expected_value = password
        assert actual_value == expected_value, f'Valor esperado de Contraseña: "{expected_value}", valor actual: "{actual_value}"'

