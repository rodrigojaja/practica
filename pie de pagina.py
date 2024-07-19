from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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

# Buscar el pie de página
element = driver.find_element(By.TAG_NAME, "footer")

# Desplazar el pie de página a la vista
driver.execute_script("arguments[0].scrollIntoView();", element)

# Comprobar que el pie de página contiene el string 'Around'
assert 'Around' in element.text
time.sleep(15)

driver.quit()