from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/droppable")
driver.maximize_window()
sleep(2)

drag=driver.find_element(By.ID,'draggable')
drop=driver.find_element(By.ID,'droppable')

action=ActionChains(driver)

action.drag_and_drop(drag,drop).perform()
sleep(2)

assert drop.text=="Dropped!"
print("drag and drop done")
driver.quit()