from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(3)
search_bar = driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
print('search bar working fine')

amazon_logo = driver.find_element(By.CSS_SELECTOR, '#nav-logo-sprites')
print('logo working fine')

cart = driver.find_element(By.CSS_SELECTOR, 'span[class="nav-cart-icon nav-sprite"]')
print('cart working fine')

sign_in = driver.find_element(By.CSS_SELECTOR, 'div[id="nav-tools"] div[class="nav-line-1-container"] span[id="nav-link-accountList-nav-line-1"]')
print('sign in working fine')

main = driver.find_elements(By.CSS_SELECTOR, 'div[id="nav-xshop"] a')
print(len(main))
print('main category links working fine')


driver.quit()