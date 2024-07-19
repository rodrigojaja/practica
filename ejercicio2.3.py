from selenium.webdriver.common.by import By


class RegistrationPageAround:
    # El localizador del campo Correo electrónico
    email_field = (By.XPATH,'//*[@id="root"]/div/div[1]/form/div[1]/label[1]')
    # El localizador del campo Contraseña
    password_field = (By.XPATH, '//*[@id="root"]/div/div[1]/form/div[1]/label[2]')
    # El localizador del botón Registrarse
    registration_button = (By.XPATH, '//*[@id="root"]/div/div[1]/form/div[2]/button')

    # El constructor de clase
    def __init__(self, driver):
        self.driver = driver

    # El método rellena el campo Correo electrónico
    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    # El método rellena el campo Contraseña
    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    # El método hace clic en el botón Registrarse
    def click_registration_button(self):
        self.driver.find_element(*self.registration_button).click()

    # El método de registro: combina el correo electrónico, la contraseña y el clic
    def register(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_registration_button()
