from selenium import webdriver
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()

uname = driver.find_element(By.XPATH, '//input[@name="username"]')
print('username is working fine')

pwd = driver.find_element(By.XPATH, '//input[@id="password"]')
print('password is working fine')

login = driver.find_element(By.XPATH, '//button[@type="submit"]')
print('login is working fine')

ele_selenium = driver.find_element(By.XPATH, '//a[text()="Elemental Selenium"]')
print('elemental selenium is working fine')

login_page = driver.find_element(By.XPATH, '//h2[contains(text(),"Login Page")]')
print('heading is working fine')

driver.quit()