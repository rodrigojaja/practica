from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()


#def test_sum():
driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es')
assert '/signin' in driver.current_url
element = driver.find_element(By.XPATH, ".//img")

driver.quit()

print(element)