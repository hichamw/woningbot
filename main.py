from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pause, datetime





import time

from selenium.webdriver.support.wait import WebDriverWait

woning = "https://www.woonnetrijnmond.nl/reageren/rotterdam/centrum/nieuwe-binnenweg-30g/100067533"

PATH = "C:\Program Files (x86)\chromedriver.exe"
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"
driver = webdriver.Chrome(desired_capabilities=caps, executable_path=PATH)

driver.get("https://www.woonnetrijnmond.nl/")

driver.find_element_by_class_name("header-secondary__btn--login").click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
time.sleep(1)
driver.find_element_by_id("username").send_keys("")
driver.find_element_by_id("password").send_keys("")
driver.find_element_by_class_name("js-submit-button").click()

pause.until(datetime.datetime(2020, 12, 17, 17, 55))

driver.get(woning)

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "btnSave")))
driver.find_element_by_id("btnSave").click()

