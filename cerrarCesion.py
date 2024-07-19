from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el driver de Chrome
driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Rellenar el campo Correo electrónico
email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
email_field.send_keys("royernene321@gmail.com")

# Rellenar el campo Contraseña
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("sexo")

# Hacer clic en el botón Iniciar sesión
login_button = driver.find_element(By.CLASS_NAME, "auth-form__button")
login_button.click()

# Esperar a que se cargue la página de inicio de sesión exitosa
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Verificar que el botón de cerrar sesión está presente y su texto es 'Cerrar sesión'
logout_button = driver.find_element(By.CLASS_NAME, "header__logout")
assert logout_button.text == 'Cerrar sesión'

# Cerrar el navegador al finalizar
driver.quit()