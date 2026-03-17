from selenium import webdriver
from selenium.webdriver.common.by import By
# action change,keys,By
from time import sleep
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts) #will not let the browser to close AUTOMATICALLY

# driver.get('https://testautomationpractice.blogspot.com')
# driver.maximize_window()
#working with text field
# name=driver.find_element(By.ID,'name')
# name.send_keys('Anjali')
# sleep(2)
# name.clear()
# name.send_keys('Rakhi')
# sleep(2)
#
# Email=driver.find_element(By.XPATH,'//input[@placeholder="Enter EMail"]')
# Email.send_keys('rakhi@gmail.com')
# sleep(2)
#
# print(name.get_attribute('placeholder'))
# print(name.get_attribute('value'))

#working eith radiobutton
# male=driver.find_element(By.ID,'male').click()
# sleep(2)
#
# #working with checkbox
# monday=driver.find_element(By.XPATH,'//label[text()="Monday"]/preceding-sibling::input').click()
# sleep(2)
#
# monday_checkbox=driver.find_element(By.XPATH,'//input[@id="monday"]/following-sibling::label')
# print(monday_checkbox.text)

# lst=['male','female']
# for i in lst:
#     gender=driver.find_element(By.ID,i).click()
#     sleep(2)
# days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
# for i in days:
#     checkbox = driver.find_element(By.XPATH, f"//label[text()='{i}']/preceding-sibling::input")
#     checkbox.click()
#     sleep(1)
# for i in reversed(days):
#     checkbox = driver.find_element(By.XPATH, f"//label[text()='{i}']/preceding-sibling::input")
#     checkbox.click()
#     sleep(1)






# driver.get('https://myntra.com')
# driver.maximize_window()
#
# search=driver.find_element(By.XPATH, '//input[@placeholder="Search for products, brands and more"]')
# search.clear()
# # search.send_keys('Dress')
# # sleep(2)
#
# # search_button=driver.find_element(By.CLASS_NAME, 'desktop-submit')
# # search_button.click()
# search.send_keys('Dress',Keys.ENTER)
# sleep(2)

# driver.get('https://www.amazon.in/')
# driver.maximize_window()
#
# search=driver.find_element(By.CSS_SELECTOR,'input[placeholder="Search Amazon.in"]')
# search.clear()
# search.send_keys('Dress', Keys.ENTER)
# sleep(2)
driver.get('https://www.flipkart.com/')
driver.maximize_window()

search=driver.find_element(By.XPATH,"//input[@placeholder='Search for Products, Brands and More']")
search.send_keys('mobiles')
print(search.get_attribute('value'))
search.send_keys(Keys.ENTER)
sleep(2)

apple=driver.find_element(By.CLASS_NAME,'buvtMR')
print(apple.text)
apple.click()
sleep(2)

image=driver.find_elements(By.XPATH,'//div[@class="lWX0_T"]/child::img')
print(image[0].is_displayed())
print(image[0].is_enabled())
print(image[0].get_attribute('src'))

driver.quit()
