from selenium icd ort webdriver
from selenium import webdriver 
import chromedriver_autoinstaller 
import undetected_chromedriver as uc 

# driver = webdriver.Firefox()

# driver.get("https://www.leboncoin.fr/recherche?category=13&text=local&locations=Lille__50.6334776434461_3.0611980440479085_9881_5000")

driver = uc.Chrome()
driver.get('https://distilnetworks.com')