from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
import time

path = Service(r'C:/Users/gomez/Downloads/edgedriver_win64.exe')
driver = webdriver.Edge(service=path)
website ='https://www.adamchoi.co.uk/teamgoals/detailed'
driver.get(website)

all_matches_button = driver.find_element("xpath", '//label[@analytics-event="All matches"]')
all_matches_button.click()

caja = driver.find_element(By.CLASS_NAME, 'panel-body')

dropdown = Select(caja.find_element(By.ID, "country"))
dropdown.select_by_visible_text('Turkey')

time.sleep(5)

matches = driver.find_elements(By.TAG_NAME, 'tr')

partidos = []
for match in matches:
    partidos.append(match.text)

driver.quit()

#PANDAS
df = pd.DataFrame({'partidos':partidos})
print(df)
df.to_csv('partidos.csv', index=False)


#input("Esperando que no se cierre webdriver: ")
