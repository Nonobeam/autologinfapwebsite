import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from flask import Flask
import os


# text = textract.process("./user-pass.doc")
# sleep(2)

login_page = "https://fap.fpt.edu.vn/Default.aspx"
# page = "https://fap.fpt.edu.vn/Report/ScheduleOfWeek.aspx"


email = "phucnhse183026@fpt.edu.vn"
password = "Haha123456"

options = Options()
options.add_argument("--window-size=1920,1080")
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options = options)
driver.get(login_page)

#choose the campus

#select campus
driver.find_element("xpath", "//select[@name='ctl00$mainContent$ddlCampus']").click()
sleep(1)

#select HCM campus
driver.find_element("xpath", "//option[@value='4']").click()
sleep(1)

#select Sign in button
driver.find_element("xpath","//div[@class='abcRioButtonContentWrapper']").click()
sleep(1)

windows = driver.window_handles
driver.switch_to.window(windows[1])

driver.find_element(By.NAME, "identifier").send_keys(email)
sleep(2)
driver.find_element(By.ID, "identifierNext").click()
sleep(2)
driver.find_element(By.NAME, "password").send_keys(password)
sleep(2)
driver.find_element(By.ID, "passwordNext").click()
sleep(15)

driver.switch_to.window(windows[0])

driver.find_element("xpath","//a[@href='Report/ScheduleOfWeek.aspx']").click()



# userAccount = driver.find_element("xpath","//*[text() = 'Nguyen Huu Phuc (K18 HCM)' ]").click()

# driver.find_element(By.NAME, "identifier").send_keys(email)
# sleep(3)
# driver.find_element(By.ID, "identifierNext").click()
# sleep(2)
# driver.find_element(By.NAME, "password").send_keys(password)
# sleep(2)
# driver.find_element(By.ID, "passwordNext").click()


sleep(999999)
# resp = requests.get(page)

# soup = BeautifulSoup(resp.content, "html.parser")
# link1 = soup.select('.row > .col-md-12')
# link2 = link1.find("form" , {"id" : "aspnetForm"})
# link3 = link2.select('.table > .tbody')
# link4 = link3.find('.tr')
# print(link1)

#problem with utf-8




