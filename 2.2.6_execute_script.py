import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/execute_script.html"

try:
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()

    driver.get(link)
    time.sleep(1)

    result = lambda x : str(math.log(abs(12*math.sin(int(x)))))

    x = driver.find_element(By.ID, "input_value").text

    driver.find_element(By.ID, "answer").send_keys(result(x))
    driver.find_element(By.ID, "robotCheckbox").click()
    driver.execute_script("window.scrollBy(0, 50);")
    time.sleep(0.5)
    driver.find_element(By.ID, "robotsRule").click()
    time.sleep(0.5)

    button = driver.find_element(By.CLASS_NAME, "btn-primary")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    time.sleep(15)
finally:
    driver.quit()
    