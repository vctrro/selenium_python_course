import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://suninjuly.github.io/explicit_wait2.html"

try:
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    driver.get(link)
    button = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    driver.find_element(By.ID, "book").click()

    result = lambda x : str(math.log(abs(12*math.sin(int(x)))))
    x = driver.find_element(By.ID, "input_value").text
    driver.find_element(By.ID, "answer").send_keys(result(x))

    button = driver.find_element(By.ID, "solve")
    button.click()

    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(": ")[-1])
    alert.accept()

finally:
    driver.quit()
    