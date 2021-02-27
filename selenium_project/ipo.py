from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome(executable_path="/Users/romanregmi/Desktop/selenium_project/driver/chromedriver")


driver.get("https://meroshare.cdsc.com.np/#/login")

wait = WebDriverWait(driver, 60)

wait.until(ec.presence_of_element_located((By.XPATH, '//span[@class="select2-selection__placeholder"]'))).click()


driver.find_element(By.XPATH, '//input[@class="select2-search__field"]').send_keys('GLOBAL IME CAPITAL LIMITED (11200)')
driver.find_element(By.XPATH, '//input[@class="select2-search__field"]').send_keys(Keys.RETURN)

driver.find_element(By.XPATH, '//input[@id="username"]').send_keys('') #input your username
driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('') #input your password
driver.find_element(By.XPATH, '//button[@class="btn sign-in"]').click()

time.sleep(3)

driver.find_element(By.XPATH, '//i[@class="msi msi-asba"]').click()

time.sleep(5)


driver.quit()
