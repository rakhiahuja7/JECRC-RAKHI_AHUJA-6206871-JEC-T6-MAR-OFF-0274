import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
actions = ActionChains(driver)
driver.maximize_window()
sleep(2)
#to the bottom of the page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(2)
#to the origin of the page
driver.execute_script("window.scrollTo(0,0);") #exact location
sleep(2)
#using scroll by
driver.execute_script("window.scrollBy(0,500);")
sleep(2)

#scrolling to element
ele = driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"])[3]/descendant::img')
driver.execute_script("arguments[0].scrollIntoView();",ele)
sleep(2)
#clicking
click_ele=driver.find_element(By.XPATH,'//div[text()="Join Pinterest"]')

driver.execute_script("arguments[0].click();",click_ele)
sleep(2)

driver.quit()
print('done')