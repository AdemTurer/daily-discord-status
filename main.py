import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = "E:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
driver = webdriver.Chrome(PATH, options=options)

file_1 = open("userE.txt", "r")
file_2 = open("userP.txt", "r")
userE = file_1.readline()
userP = file_2.readline()
file_1.close()
file_2.close()

driver.get("https://discord.com/login")

emailField = driver.find_element(By.XPATH, "//div/input[@name='email']")
emailField.send_keys(userE)

passwordField = driver.find_element(By.XPATH, "//div/input[@name='password']")
passwordField.send_keys(userP)

loginBtn = driver.find_element(By.XPATH, "//button/div[text()='Login']/..")
loginBtn.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@aria-label, 'Set Status')]"))
    )
except:
    print("the element wasn't found during the exception timeout period")
    driver.quit()

listOfWords = ["hi there!", "you're probably", "wondering", "how I ended up", "in this ", "sticky situation",
              "well, it all started", "when I had the", "brilliant idea of", "writing a script", "that would change",
              "my discord status", "in a loop", "ha ha", "I need a hobby", "jesus christ"]

def statusChanger(myList):
    for i in range(len(listOfWords)):
        setStatusBtn = driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Set Status')]")
        setStatusBtn.click()

        setStatusBtn2 = driver.find_element(By.XPATH, "//span[@class='customText-36Uwzc']")
        setStatusBtn2.click()

        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'inputWrapper-1YNMmM')]/input"))
            )
        except:
            print("the element wasn't found during the exception timeout period")
            driver.quit()

        statusContainer = driver.find_element(By.XPATH, "//div[contains(@class, 'inputWrapper-1YNMmM')]/input")
        statusContainer.clear()
        statusContainer.send_keys(myList[i])

        saveBtn = driver.find_element(By.XPATH, "//button/div[contains(text(),'Save')]/..")
        saveBtn.click()

while True:
    statusChanger(listOfWords)
    time.sleep(1)

#driver.quit()