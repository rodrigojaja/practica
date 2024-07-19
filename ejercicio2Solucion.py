import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Inicializar el WebDriver
driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

try:
    # Iniciar sesión
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    email_field.send_keys("royernene321@gmail.com")
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("sexo")
    login_button = driver.find_element(By.CLASS_NAME, "auth-form__button")
    login_button.click()

    # Esperar a que se cargue el feed
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "places__list")))

    # Guardar el título de la tarjeta más reciente
    title_before = driver.find_element(By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']").text

    # Hacer clic en el botón que publica una nueva tarjeta
    driver.find_element(By.CLASS_NAME, "profile__add-button").click()

    # Ingresar el nombre del nuevo lugar; debe ser diferente de la tarjeta más reciente
    new_title = f"Tokio{random.randint(100, 999)}"
    driver.find_element(By.NAME, "name").send_keys(new_title)

    # Insertar un enlace a la nueva foto
    driver.find_element(By.NAME, "link").send_keys(
        "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/photoSelenium.jpg")

    # Guardar los datos
    driver.find_element(By.XPATH, ".//form[@name='new-card']/button[text()='Guardar']").click()

    # Esperar a que aparezca el botón que elimina la publicación
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//li[@class='places__item card'][1]/button[@class='card__delete-button card__delete-button_visible']")))

    # Comprobar que la tarjeta tiene el título correcto aaaaaaaaaaaaaaaaaaaa espero poder con el proyecto es importante andar compruebe ycompruebe todo
    title_after = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/div[2]/h2')
    otro = driver.find_element(By.XPATH, "//li[@class='places__item card']//h2[@class='card__title']")
    print(otro.text)
    print(title_after.text)
    if(title_after.text == otro.text):
        print("son iguales",title_after.text, otro.text)
    assert title_after.text == new_title

    # Guardar la cantidad de tarjetas antes de eliminar
    cards_before = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))
    otras = len(driver.find_elements(By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li'))
    print(cards_before)
    print(otras)
    if(cards_before ==otras):
        print("sisi son iguales")

    # Eliminar la tarjeta
    driver.find_element(By.XPATH,
                        "//li[@class='places__item card'][1]/button[@class='card__delete-button card__delete-button_visible']").click()

    # Esperar a que desaparezca el título de la tarjeta eliminada
    WebDriverWait(driver, 10).until(EC.staleness_of(title_after))

    # Comprobar que ahora hay una tarjeta menos
    cards_after = len(driver.find_elements(By.XPATH, "//li[@class='places__item card']"))
    otras = len(driver.find_elements(By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li'))
    print(cards_after, otras)
    assert cards_before - otras == 1

finally:
    # Cerrar el WebDriver al finalizar
    driver.quit()