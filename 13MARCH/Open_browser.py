from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
#
# # opts.add_argument('--headless')
#
driver=webdriver.Chrome(options=opts)
#
driver.get('https://testautomationpractice.blogspot.com')
driver.maximize_window()

# sleep(3)
# name=driver.find_element(By.ID,'name')
# Navbar=driver.find_element(By.NAME,'Navbar')
# radio_button=driver.find_element(By.CLASS_NAME,'form-check-input')
# inp=driver.find_element(By.TAG_NAME,'input')
# # print('its working')
# # print(name)
# print(inp)
# print(radio_button)
# print(Navbar)
# # print(len(radio_button))
# # print('name textfield found')
#
# driver.quit()


# driver=webdriver.Chrome(options=opts)
# driver.get('https://google.com/')
# driver.maximize_window()
# sleep(2)
#
# print('by id: ')
# dialog=driver.find_element(By.ID,'spch-dlg')
# print('dialog is: ', dialog)
# sph=driver.find_element(By.ID,'spch')
# print('sph is: ', sph)
# pages=driver.find_elements(By.ID,'gws-output-pages-elements-homepage_additional_languages__als')
# print('pages is: ', pages)
# cob=driver.find_element(By.ID,'SIvCob')
# print('cob is: ', cob)
# lb=driver.find_element(By.ID,'lb')
# print('lb is: ', lb)
#
# print('by name: ')
# theme_color = driver.find_element(By.NAME, 'theme-color')
# print(theme_color)
# viewport = driver.find_element(By.NAME, 'viewport')
# print(viewport)
# keyword = driver.find_element(By.NAME, 'keywords')
# print(keyword)
# desc = driver.find_element(By.NAME, 'description')
# print(desc)
#
# print('by class-name: ')
# lb=driver.find_element(By.CLASS_NAME,'gTMtLb')
# print('lb is: ', lb)
# one=driver.find_element(By.CLASS_NAME,'vcVZ7d')
# print('one is: ', one)
# csi=driver.find_element(By.CLASS_NAME,'csi')
# print('csi is: ', csi)
# div=driver.find_element(By.CLASS_NAME,'OLKT8d')
# print('div is: ', div)
# apps=driver.find_element(By.CLASS_NAME,'gb_L')
# print('apps is: ', apps)
#
## using css selectors
# 'tag_name[attribute = 'value']' and can also use symbols like for id - #, class - .
# name = driver.find_element(By.CSS_SELECTOR, 'select[id="animals"]')
# animals = driver.find_element(By.CSS_SELECTOR, '#animals')

# form_group = driver.find_elements(By.CSS_SELECTOR, '.form-group')
# form_group = driver.find_elements(By.CSS_SELECTOR, "div[class='form-group]")


print('worked fine')

# driver.quit()

# <a href="https://testautomationpractice.blogspot.com/">Home</a>

# div[class="widget-content"]
# div[class="widget-content"] a[href*="testautomationpractice.blogspot.com/"]

## XPATH
## can go backwards or upwards and downwards, can also locate inner text, but it is slower than other locators and difficult to read
## two types -- absolute path and relative path
# absolute -- /html/body/..../tag_name[@attribute = 'value']
# relative path -- //tag_name[@attribute = 'value'] [index]
# can use indexing if there are multiple elements


male = driver.find_element(By.XPATH, '//input[@type="radio"][1]')
print("worked fine")

phone_no = driver.find_element(By.XPATH, '//input[@maxLength="10"]')
print("worked fine")

value=driver.find_element(By.XPATH, '//option[@value="canada"]')
print("worked fine")

udemy=driver.find_element(By.XPATH, '//a[text()="Udemy Courses"]')
print("worked fine")

female=driver.find_element(By.XPATH, '//label[text()="Female"]')
print("worked fine")

japan=driver.find_element(By.XPATH, '//option[contains(text(),"Japan")]')
print("worked fine")




driver.quit()