# Everything we will need from Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# other imports here
import os
import wget


# Login to our Instagram
driver = webdriver.Chrome(
    'C:/Users/Shakes/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("https://www.instagram.com/")

# Target the username and password. Extracted from dev tools
# wait for CSS, JS, etc to load before we insert keys
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input[name='username']")))  # Grab element by CSS selector
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# make sure the fields are empty
username.clear()
password.clear()

# write the folloeing automativally
username.send_keys("iamthegeorgebest")
password.send_keys("3ll1psis")

# Tap the submit button
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']"))).click()

# First not now prompt
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

# Second not now prompt
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

# Tapping into searchbox
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@placeholder='Search']"))).click()

# Clear the searchbox
searchbox.clear()

# What to search for
keyword = "#ecommerce"
searchbox.send_keys(keyword)
searchbox.send_keys(Keys.ENTER)

driver.execute_script("window.scrollTo(0, 4000);")

images = [image.get_attribute('src') for image in images]
images.driver.find_elements_by_tag_name('img')


# Save images to computer
path = os.getcwd()
# have each image be saved using keyword
path = os.path.join(path, keyword[1:] + " pic")

# Send them to this directory
os.mkdir(path)

# Download using wget
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
