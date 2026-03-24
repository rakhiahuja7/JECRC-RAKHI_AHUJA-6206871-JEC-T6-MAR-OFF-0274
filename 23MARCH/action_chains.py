from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys

#drag and drop
driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
# driver.maximize_window()
# sleep(3)

actions = ActionChains(driver)

# origin_ele=driver.find_element(By.ID,'column-a')
# target_ele=driver.find_element(By.ID,'column-b')
#
# actions.drag_and_drop(origin_ele,target_ele).perform()
# sleep(3)

#mouse_hover
# driver.get("https://supertails.com/")
# driver.maximize_window()
# dog=driver.find_element(By.XPATH,'(//span[contains(text(),"Dogs")])[1]')
#
# actions.move_to_element(dog).perform()
# sleep(2)

# catto=driver.find_element(By.XPATH,'//div[@data-ganame="Breed 5"]')
# actions.scroll_to_element(catto).perform()
# sleep(5)
#
# actions.scroll_by_amount(0,1500).perform()
# sleep(5)

# actions.send_keys(Keys.PAGE_DOWN).perform()
# sleep(5)
#
# actions.send_keys(Keys.PAGE_UP).perform()
# sleep(5)
#
# actions.key_down(Keys.CONTROL).perform()
# sleep(5)
#
# actions.send_keys(Keys.CONTROL).send_keys('a').perform()
# sleep(5)
#
# actions.key_up(Keys.CONTROL).perform()
# sleep(5)

# copying and pasting for address fields

# driver.get(r"C:\Users\Ahuja's\OneDrive\Desktop\sellenium\Project\JECRC\23MARCH\address_field.html")
# driver.maximize_window()
#
# present=driver.find_element(By.ID,'presentAddress')
# permanent=driver.find_element(By.ID,'permanentAddress')
#
# present.send_keys('JECRC,Jaipur')
# sleep(2)
# present.click()
# actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# sleep(2)
# actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# permanent.click()
# sleep(2)
# actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# sleep(2)

# password visibility

driver.get(r"C:\Users\Ahuja's\OneDrive\Desktop\sellenium\Project\JECRC\23MARCH\index1.html")
driver.maximize_window()

driver.find_element(By.ID,'password').send_keys("Rakhi")
sleep(2)
show_pwd = driver.find_element(By.ID,'eyeBtn')
actions.click_and_hold(show_pwd).perform()
sleep(2)
actions.release()
