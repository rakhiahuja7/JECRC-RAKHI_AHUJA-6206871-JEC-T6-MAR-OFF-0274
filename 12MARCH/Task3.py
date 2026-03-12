from selenium import webdriver
from time import sleep

List1 = [webdriver.Chrome(), webdriver.Edge(), webdriver.Firefox()]

for i in List1:
    driver = i
    sleep(5)
    driver.get('https://amazon.com/')
    sleep(3)
    print(f'The url is: {driver.current_url}')
    print(f'The title is: {driver.title}')
    print(f'The name of browser is: {driver.name}')
    driver.quit()