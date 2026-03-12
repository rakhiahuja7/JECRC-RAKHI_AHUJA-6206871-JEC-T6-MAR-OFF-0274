from selenium import webdriver
from time import sleep
# driver.get('https://supertails.com/')
# driver.get('https://topbrains.com/')
# driver.maximize_window()
# sleep(4)
# driver.minimize_window()
# sleep(5)

# driver.back()
# sleep(3)
# driver.forward()
# sleep(3)
# driver.refresh()
# sleep(3)

# driver.close()
# driver.quit()

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://amazon.com/')
print(driver.title)
print(f'The title is : {driver.title}')
print(f'The url is : {driver.current_url}')
print(f'The name of browser is: {driver.name}')