import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = "E:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

file_1 = open("userE.txt", "r")
file_2 = open("userP.txt", "r")
userE = file_1.readline()
userP = file_2.readline()
file_1.close()
file_2.close()

driver.get("https://discord.com")
time.sleep(2)
loginBtn = driver.find_element(By.XPATH, '//div[@class="mobileButtonContainer-JUZBON"]/a')
loginBtn.click()



time.sleep(2)
#driver.quit()