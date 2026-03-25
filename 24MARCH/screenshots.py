import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

folder = os.path.join(os.getcwd(), 'screenshots')  #current working directory
os.makedirs(folder, exist_ok=True)

driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
actions = ActionChains(driver)
driver.maximize_window()

sleep(2)

driver.save_screenshot(f'{folder}/screenshot.png')
sleep(2)

ele=driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"])[3]/descendant::img')
actions.scroll_to_element(ele).perform()

ele.screenshot(f'{folder}/screenshot_pic.png')
sleep(2)

driver.quit()
print('done')
