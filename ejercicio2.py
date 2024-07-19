import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

# Guardar el título de la tarjeta más reciente
try:
    title_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/div[2]')))
    title_before = title_element.text
    print("Título de la tarjeta más reciente:", title_before)
except Exception as e:
    print("Error al encontrar el elemento:", e)

driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/button').click()
driver.find_element(By.XPATH, '//*[@id="place-name"]').send_keys("wasa")

driver.find_element(By.XPATH, '//*[@id="place-link"]').send_keys("https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg")

driver.find_element(By.XPATH, '//*[@id="place-description"]').send_keys("wasaweb")

driver.find_element(By.XPATH, '//*[@id="place-address"]').send_keys("porahinomas")

driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/form/button[2]').click()

print(driver.find_element(By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']").text)
#assert driver.find_element(By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']").text == "wasa"
#assert driver.find_element(By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']").text == 'wasa'
#cards_before = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))


#Hacer clic en el botón que publica una nueva tarjeta
#driver.find_element(...)...

# Generar el nuevo nombre del lugar e ingresarlo en el campo Nombre
#new_title = ...
#driver.find_element(...)...

# Insertar el enlace a la imagen en el campo Enlace
#driver.find_element(...)...

# Guardar los datos
#driver.find_element(...)...

# Esperar a que aparezca el botón Eliminar
#WebDriverWait(...).until(...)

# Comprobar que la tarjeta tiene el título correcto
#title_after = ...
#assert ...

# Guardar la cantidad de tarjetas antes de eliminar
#cards_before = len(...)

# Eliminar la tarjeta
#driver.find_element(...)...

# Esperar a que el título de la tarjeta más reciente sea igual a title_before
#WebDriverWait(...).until(...)

# Comprobar que ahora hay una tarjeta menos
#cards_after = len(...)
#assert ...
time.sleep(5)

driver.quit()