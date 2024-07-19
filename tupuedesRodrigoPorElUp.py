from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Iniciar sesión
# Rellenar el campo Correo electrónico
email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
email_field.send_keys("royernene321@gmail.com")

# Rellenar el campo Contraseña
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("sexo")

# Hacer clic en el botón Iniciar sesión
login_button = driver.find_element(By.CLASS_NAME, "auth-form__button")
login_button.click()
# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "header__user")))
# Hacer clic en la foto de perfil
driver.find_element(By.XPATH, "//div[@class='profile__image']").click()

avatar_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"
# Insertar el enlace a la foto en el campo Enlace utilizando la variable avatar_url
driver.find_element(By.XPATH, '//*[@id="owner-avatar"]').send_keys(avatar_url)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/form/button[2]').click()



# Guardar la nueva foto
#driver.find_element(...)...

# Guardar el valor del atributo de estilo para el elemento de foto de perfil en la variable style
style = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]').get_attribute('style')
print(style)
# Comprobar que style contiene el enlace a la foto de perfil
assert 'https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png' in style
#vari = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/div[2]/h2/font/font')
#print(vari.text)
time.sleep(15)

driver.quit()