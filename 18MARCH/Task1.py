from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()

checkbox = driver.find_element(By.LINK_TEXT, 'Checkboxes')
print('found')
sleep(3)

drag_n_drop = driver.find_element(By.PARTIAL_LINK_TEXT, 'Drag')
print('found')
sleep(3)

list_items= driver.find_elements(By.TAG_NAME, 'li')
print(len(list_items))
sleep(3)

driver.get('https://the-internet.herokuapp.com/tables')
sleep(1)

web_site = driver.find_element(By.XPATH, '(//td[text() = "jdoe@hotmail.com"][1]/following-sibling::td[2])[1]')
print('found')
sleep(2)

delete_link = driver.find_element(By.XPATH, '(//td[text() ="Bach"][1]/following-sibling::td[5])[1]/descendant::a[2]')
print('found')
sleep(3)

sec_table = driver.find_element(By.XPATH, '//table[2]')
print('found')
sleep(3)

dues = driver.find_element(By.XPATH, '//table[@id="table2"]/child::tbody/child::tr[3]/child::td[4]')
print('found')
sleep(3)

driver.quit()