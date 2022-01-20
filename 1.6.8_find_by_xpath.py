import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/find_xpath_form"

try:
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()

    driver.get(link)
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("Vc")
    driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Ro")
    driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Mo")
    driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Ro")

    button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    time.sleep(15)
finally:
    driver.quit()
    