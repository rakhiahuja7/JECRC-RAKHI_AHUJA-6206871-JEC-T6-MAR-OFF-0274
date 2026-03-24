# Task2
# 0pen myntra
# hover over men or women
# choose a category then click on it
# scroll to 4th or 5th row product
# use proper waits

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
actions = ActionChains(driver)

driver.get('https://www.myntra.com/')
driver.maximize_window()
sleep(2)
wait = WebDriverWait(driver, 10)

women = wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@class="desktop-navLink"]/child::a[@data-group="women"]')))
actions.move_to_element(women).perform()

category = driver.find_element(By.XPATH, '//div[@class = "desktop-categoryContainer"]/descendant::ul[@class= "desktop-navBlock"]/descendant::li[@data-reactid="191"]').click()
sleep(4)

fifth_row = driver.find_element(By.ID, '35157650')
sleep(2)
actions.scroll_to_element(fifth_row).perform()
sleep(3)

driver.quit()

