from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
waitTime1 = 15
waitTime2 = 3602
def GetFreeCase():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--user-data-dir=C:/Users/Lenovo/AppData/Local/Google/Chrome/User Data/Default")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://dealskins.com/case/cash")
    try:
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "btnOpen")))
    finally:
        element_value = driver.find_element_by_class_name("header_input")
        driver.find_element_by_id("btnOpen").click();
        time.sleep(waitTime1)
        print(str(time.strftime("%H:%M:%S") + ' - ' + element_value.get_attribute("value")))
        driver.quit()
def OpenCase():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--user-data-dir=C:/Users/Lenovo/AppData/Local/Google/Chrome/User Data/Default")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://dealskins.com/case/army")
    while True:
        try:
            element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "btnOpen")))
        except:
            pass
        else:
            try:
                element_value = driver.find_element_by_class_name("header_input")
                print(str(time.strftime("%H:%M:%S") + ' - ' + element_value.get_attribute("value")))
            finally:
                pass
            if element.text == "OPEN CASE $0.19":
                print("On sale!!")
                try:
                    element.click()
                finally:
                    pass
            else:
                print("Not on sale!!")
                driver.quit()
        finally:
            pass
        try:
            element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "btnSell")))
        except:
            pass
        else:
            try:
                driver.find_element_by_id("btnSell").click();
            finally:
                pass
        finally:
            pass
    driver.quit()
while True:
    OpenCase()

