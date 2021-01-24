from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

browser_name = "chrome"

if browser_name == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())

elif browser_name == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

elif browser_name == "safari":
    driver = webdriver.Safari()

else:
    print("Please pass the correct browser name : " + browser_name)
    raise Exception('driver is not found')

driver.implicitly_wait(10)