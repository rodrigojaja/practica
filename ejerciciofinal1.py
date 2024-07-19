from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# clase para la página de inicio de sesión
class LoginPageAround:
    email_field = (By.ID, 'email')
    password_field = (By.ID, 'password')
    sign_in_button = (By.CLASS_NAME, 'auth-form__button')

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()

# clase para la página principal
class HomePageAround:
    # Crea un localizador para el campo Ocupación en el perfil de usuario
    profile_description = (By.CLASS_NAME, 'profile__description')

    def __init__(self, driver):
        self.driver = driver

    # Espera a que se cargue la página
    # Espera a que aparezca el campo Ocupación
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.profile_description))

    # Recupera el valor del campo Ocupación
    def get_description(self):
        return self.driver.find_element(*self.profile_description).text

class TestAround:

    driver = None

    @classmethod
    def setup_class(cls):
        # Crea un controlador para Chrome
        cls.driver = webdriver.Chrome()

    def test_get_description(self):
        # Abre la página de la aplicación de prueba
        self.driver.get('https://around-v1.es.practicum-services.com/')

        # Crea una clase de objeto de página para la página de inicio de sesión
        login_page = LoginPageAround(self.driver)
        # Iniciar sesión
        login_page.login('correo electrónico', 'contraseña')

        # Crea un objeto de página para la página principal
        home_page = HomePageAround(self.driver)
        # Espera a que se cargue la página principal
        home_page.wait_for_load_home_page()
        # Guarda el valor de Ocupación en la descripción
        description = home_page.get_description()

        # Utiliza assert para comprobar que el valor actual de Ocupación coincida con el valor esperado
        assert description == 'ocupación para el perfil de usuario o usuaria'

    @classmethod
    def teardown_class(cls):
        # cerrar el navegador
        cls.driver.quit()