from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Iniciar sesión
email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
email_field.send_keys("royernene321@gmail.com")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("sexo")
login_button = driver.find_element(By.CLASS_NAME, "auth-form__button")
login_button.click()
# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Buscar la tarjeta y desplazarla a la vista
#element = driver.find_element(By.CSS_SELECTOR, ".places__item")
#element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li')
#print(element)
element = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]')
print(element)

driver.execute_script("arguments[0].scrollIntoView();", element)

# Aquí podrías realizar más acciones con el elemento visible, como hacer clic en él o verificar su contenido.
time.sleep(5)

# Finalizar la sesión del navegador
driver.quit()