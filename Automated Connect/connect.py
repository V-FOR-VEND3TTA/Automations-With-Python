"""
This script automates the process of connecting with people on LinkedIn
"""

from selenium import webdriver as wd
import time as t

# insert the file path where our drive executable is
driver = wd.Chrome(
    'C:/Users/George/Downloads/chromedriver_win32/chromedriver.exe')
# the website we want to get access to
driver.get('https://www.linkedin.com')
# wait for the page to load by the specified
t.sleep(2)

# ------------- Automated login --------------------
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

# the username used to log on
username.send_keys('georgehlongwane8@gmail.com')
# the password used to validate identity of the user
password.send_keys('V0ld3rm0rt')
# wait for specified time for page loading
t.sleep(2)

submit = driver.find_element_by_xpath("//button[type='submit']").click()

# --------------- Add Specified Contacts --------------
# the url to the search
driver.get("https://www.linkedin.com/search/results/people/")
t.sleep(2)

# access all the buttons on current page
all_buttons = driver.find_elements_by_tag_name("button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

for btn in connect_buttons:
    # JS to click on buttons because of the click button exception on LinkedIn site
    driver.execute_script("arguments[0].click();", btn)
    t.sleep(2)
    # Remove personalized message popup
    send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send)
    # for exceptions of privacy settings like "To verify this member knows you, please enter their email to connect..."
    close = driver.find_element_by_xpath("//button[aria-label='Dismiss']")
    driver.execute_script("arguments[0].click();", close)
    t.sleep(2)
