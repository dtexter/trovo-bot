from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from webdriver_manager.chrome import ChromeDriverManager
from anticaptchaofficial.recaptchav2proxyless import *

import random
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options,
)
wait = WebDriverWait(driver, 5)


class Btns:
    signup = "body > div:nth-child(8) > div > div.content-box > div.content-left > div:nth-child(1) > ul > li:nth-child(2) > span"
    email = "body > div:nth-child(8) > div > div.content-box > div.content-left > div:nth-child(1) > div:nth-child(2) > div > input"
    username = "body > div:nth-child(8) > div > div.content-box > div.content-left > div:nth-child(1) > div:nth-child(3) > div > input"
    password = "body > div:nth-child(8) > div > div.content-box > div.content-left > div:nth-child(1) > div:nth-child(4) > div > input"
    day = "body > div:nth-child(8) > div > div.content-box > div.content-left > div:nth-child(1) > div:nth-child(5) > div.content > div:nth-child(2) > div.day > input"
    month = "body > div:nth-child(8) > div > div.content-box > div.content-left > div:nth-child(1) > div:nth-child(5) > div.content > div:nth-child(1) > div.month > span"
    year = "body > div:nth-child(8) > div > div.content-box > div.content-left > div:nth-child(1) > div:nth-child(5) > div.content > div:nth-child(3) > div.year > input"
    select_month = "body > div:nth-child(8) > div > div.content-box > div.content-left > div:nth-child(1) > div:nth-child(5) > div.content > div:nth-child(1) > div.drop-list > ul > li:nth-child("
    register = "body > div:nth-child(8) > div > div.content-box > div.content-left > div:nth-child(1) > button"


def click(btn):
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, btn))).click()


def write(btn, text):
    field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, btn)))
    field.send_keys(text)


solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key("58be8d3247d7b5ac538a7280faf71ea6")

driver.get("https://cdn.trovo.live/page/login-page.html")
click(Btns.signup)
write(Btns.email, "Tester@test.com")
write(Btns.username, "Tester030")
write(Btns.password, "Tester030")
click(Btns.month)
click(Btns.select_month + str(random.randrange(1, 12)) + ")")
write(Btns.day, random.randrange(1, 27))
write(Btns.year, random.randrange(1990, 2004))
time.sleep(3)
print(driver.page_source)
solver.set_website_url(driver.current_url)
solver.set_website_key("6LfjEMoUAAAAAPv60USWs4LxOlTmoiGf7m2skV4O")
# data_sitekey = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "g-recaptcha"))).get_attribute("data-sitekey")
# print(data_sitekey)
g_response = solver.solve_and_return_solution()
if g_response != 0:
    print("g-response: " + g_response)
else:
    print("task finished with error " + solver.error_code)

driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML='{}';".format(g_response))
time.sleep(3)
click(Btns.register)
input("DONE")
