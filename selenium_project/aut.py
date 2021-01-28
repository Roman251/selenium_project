import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def buy_sell(action,user_name,password):
    print("Input the captcha yourself for now")

    driver = webdriver.Chrome(executable_path="/Users/romanregmi/Desktop/selenium_project/driver/chromedriver")

    driver.get("https://tms43.nepsetms.com.np/login")

    wait = WebDriverWait(driver, 60)
    user = wait.until(ec.presence_of_element_located((By.XPATH, '//input[@placeholder="Client Code/ User Name"]')))
    user.send_keys(user_name)

    driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(password)

    # =============================================================================
    # img = driver.find_element(By.XPATH,'//input[@id="randomfield"]')
    # img.screenshot('captcha.png')
    # 
    # time.sleep(10)
    # =============================================================================



    # =============================================================================
    # import easyocr
    # from pylab import rcParams
    # 
    # rcParams['figure.figsize'] = 8, 16
    # 
    # reader = easyocr.Reader(['en'])
    # output = reader.readtext('captcha.png')
    # print(output)
    # 
    # text_key = output[0][1]
    # 
    # driver.find_element(By.ID, 'captchaEnter').send_keys(text_key)
    # =============================================================================

    time.sleep(10)

    driver.find_element(By.XPATH, '//input[@value="Login"]').click()

    time.sleep(5)

    new_url = driver.current_url

    driver.get(new_url)

    driver.find_element(By.XPATH, '//span[text()="Order Management"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//span[text()="Buy/Sell "]').click()

    time.sleep(25)

    url = driver.current_url

    print(url)

    driver.get(url)

    driver.implicitly_wait(10)
    

    if action == "B":
        driver.find_elements(By.XPATH, '//label[@class="xtoggler-btn-wrapper"]')[1].click()
    else:
        driver.find_elements(By.XPATH, '//label[@class="xtoggler-btn-wrapper"]')[0].click()

    time.sleep(3)

    driver.quit()



buy_sell('Buy',2020094320,'')
