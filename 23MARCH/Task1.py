# Task1
# open fav ipl site
# scroll fav pic
# use for loop to go to up 5 times using page up

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

actions = ActionChains(driver)

driver.get("https://www.royalchallengers.com/rcb-squad-men")
driver.maximize_window()
sleep(2)

jitesh =driver.find_element(By.XPATH,'(//div[@class="media media--blazy media--switch media--switch--content media--bundle--image media--image is-b-loaded"])[10]')
actions.scroll_to_element(jitesh).perform()
sleep(5)

for i in range(0,5):
    actions.send_keys(Keys.PAGE_UP).perform()
    sleep(1)



