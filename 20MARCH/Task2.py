from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get(r"C:\Users\Ahuja's\OneDrive\Desktop\sellenium\Project\JECRC\20MARCH\playlist.html")
driver.maximize_window()

song_list =driver.find_element(By.ID, 'songs')
select = Select(song_list)

if select.is_multiple:
    dua=driver.find_elements(By.XPATH,'//optgroup[@label="Dua Lipa"]/descendant::optionchro')
    for i in dua:
        select.select_by_visible_text(i.text)

print([i.text for i in select.all_selected_options])
sleep(3)


driver.find_element(By.XPATH, '//button[text() = "Add to Playlist"]').click()
sleep(3)

driver.quit()