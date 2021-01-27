from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

my_companies = pd.read_csv('cns.csv')

def get_vis(dta):

    print("The data being used to decide the selling/buying procedure is taken from the chart present in this site.")

    # time.sleep(2)

    driver = webdriver.Chrome(executable_path="/Users/romanregmi/Desktop/selenium_project/driver/chromedriver")

    driver.get("http://nepalstockinfo.com/chart/nepse")

    time.sleep(5)

    # companies_list = driver.find_elements(By.XPATH, '//div[@class="dropdown-menu open"]//ul[@class="dropdown-menu inner"]//span[@class="text"]')
    # comapnies_list = companies_list[0:361]

    # for items in comapnies_list:
    #     print(items.text)

    for cn in my_companies['init']:
        for ele in dta:
            if cn == ele:
                driver.find_element(By.XPATH, '//span[@class="bs-caret"]//span[@class="caret"]').click()
                driver.find_element(By.XPATH,'//div[@class="dropdown-menu open"]//input[@class="form-control"]').send_keys(cn)
                driver.find_element(By.XPATH,'//div[@class="dropdown-menu open"]//input[@class="form-control"]').send_keys(Keys.RETURN)
                time.sleep(5)
                driver.back()
                time.sleep(5)
                break
    
    driver.quit()