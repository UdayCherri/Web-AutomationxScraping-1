from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com/")
search=driver.find_element(By.ID, 'APjFqb')
search.send_keys("Justin Bieber")
search.send_keys(Keys.ENTER)

insta = driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[1]/div/div/span/a/h3')
insta.click()

time.sleep(100)

driver.close()