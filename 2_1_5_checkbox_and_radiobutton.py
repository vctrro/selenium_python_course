import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"

try:
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()

    driver.get(link)
    time.sleep(2)

    result = lambda x : str(math.log(abs(12*math.sin(int(x)))))

    x = driver.find_element(By.ID, "input_value").text

    driver.find_element(By.ID, "answer").send_keys(result(x))
    driver.find_element(By.ID, "robotCheckbox").click()
    driver.find_element(By.ID, "robotsRule").click()

    button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    time.sleep(15)
finally:
    driver.quit()
    