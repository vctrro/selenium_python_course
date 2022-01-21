import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/alert_accept.html"

try:
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()

    driver.get(link)
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, "btn-primary").click()

    time.sleep(0.5)
    driver.switch_to.alert.accept()

    result = lambda x : str(math.log(abs(12*math.sin(int(x)))))
    x = driver.find_element(By.ID, "input_value").text
    driver.find_element(By.ID, "answer").send_keys(result(x))

    button = driver.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    time.sleep(0.5)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(": ")[-1])
    alert.accept()

finally:
    driver.quit()
    