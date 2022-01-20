import time

from selenium import webdriver
from selenium.webdriver.common.by import By

site_link1 = "https://suninjuly.github.io/registration1.html"
site_link2 = "https://suninjuly.github.io/registration2.html"

def test(link):
    try:
        # driver = webdriver.Firefox()
        driver = webdriver.Chrome()

        driver.get(link)
        time.sleep(2)

        #required fields
        driver.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Vc")
        driver.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("Ro")
        driver.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("vc@ro.us")
        
        #other fields
        driver.find_element(By.XPATH, "//input[@placeholder='Input your phone:']").send_keys("+1-007")
        driver.find_element(By.XPATH, "//input[@placeholder='Input your address:']").send_keys("USA")

        button = driver.find_element(By.CLASS_NAME, "btn")
        button.click()
        time.sleep(1)

        welcome_text = driver.find_element(By.TAG_NAME, "h1").text

        assert welcome_text == "Congratulations! You have successfully registered!"

    finally:
        driver.quit()

test(site_link1)
test(site_link2)
    