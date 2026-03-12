from selenium import webdriver
from time import sleep
list1=[webdriver.Chrome(),webdriver.Edge(),webdriver.Firefox()]
for i in list1:
    driver=i
    sleep(2)
    driver.quit()