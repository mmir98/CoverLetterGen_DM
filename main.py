from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 
import time
import random

cl_title = 'Application for Computer Science position'
cl_persona = 'Recruiter'
cl_keywords = ['Responsible', 'Hardworking', 'Friendly', 'Open to new challenges']

def random_short_sleep():
    time.sleep(random.randint(1, 2))

def random_long_sleep():
    time.sleep(random.randint(5, 10))

def does_element_exist(driver, xpath):
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
        print("item loaded")
        return True
    except :
        print("item not found")
        return False


def enter_text(element, text):
    for i in text:
        element.send_keys(i)
        random_short_sleep()

DRIVER_PATH = 'chromedriver.exe'
USER_DATA_DIR = 'C:\\Users\\moham\\AppData\\Local\\Google\\Chrome\\User Data'
URL = 'https://app.gomoonbeam.com/'

# titles
HOME_TITLE = 'Moonbeam - Home'
HEADSTART_TITLE = 'Moonbeam - Headstart'
WIZARD_TITLE = 'Moonbeam - Wizard'
EDITOR_TITLE = 'Moonbeam - Editor'

# XPaths
USE_WIZARD_XPATH = '//*[@id="modal-root"]/main/div/div/div[1]/div/div[1]/a[3]'
STUDENT_XPATH = '//*[@id="modal-root"]/div[1]/div/div/div[2]/div/div/div[2]/div/div[3]'
COLLEGE_ADMMISION_ESSAY_XPATH = '//*[@id="modal-root"]/div[1]/div/div/div[2]/div/div/div[2]/div/button[8]'
TITLE_IPNUT_XPATH = ' //*[@id="modal-root"]/div[1]/div/div/div[1]/div[2]/div'
PERSONA_WRITING_FOR_XPATH = '//*[@id="modal-root"]/div[1]/div/div/div[1]/div[3]/div'
ADD_KEYWORD_BASE_XPATH = '//*[@id="modal-root"]/div[1]/div/div/div[1]/div[4]/div/ul/li' #[]/p
GENERATE_OUTLINE_BUTTON_XPATH = '//*[@id="modal-root"]/div[1]/div/div/div[2]/button'
CREATE_POINTS_BUTTON_XPATH = '//*[@id="modal-root"]/div[1]/div/div/div[2]/button'
FINISHING_TOUCHES_BUTTON_XPATH = '//*[@id="modal-root"]/div[1]/div/div/div[2]/div[2]/button'
# PUBLISH_MENU_BUTTON_XPATH = '//*[@id="modal-root"]/div[2]/div/div[1]/div/div[2]/button[24]'
# COPY_CONTENT_BUTTON_XPATH = '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button'
FINAL_CONTENT_XPATH = '/html/body/div[1]/div/div[2]/div/div[1]/div/div[3]/div'

service = Service(executable_path=DRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_argument(f'user-data-dir={USER_DATA_DIR}')
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get(URL)
driver.implicitly_wait(5)


# find_element_by_xpath(USE_WIZARD_XPATH)
if not does_element_exist(driver, USE_WIZARD_XPATH):
        print("Use wizard doesnt exist")

title = driver.title
print(title)
assert title == HOME_TITLE
useWizard_el = driver.find_element(By.XPATH, USE_WIZARD_XPATH)
print(useWizard_el)
useWizard_el.click()
random_long_sleep()

# WAIT TILL THE PAGE IS FULLY LOADED
if not does_element_exist(driver, STUDENT_XPATH):
    print("student element doesn't exist")
print(driver.title)
assert driver.title == HEADSTART_TITLE
student_el = driver.find_element(By.XPATH, STUDENT_XPATH)
random_short_sleep()
student_el.click()
random_long_sleep()

# WAIT TILL THE PAGE IS FULLY LOADED
# if CAE is not visible scroll
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
random_short_sleep()
collegeAdmmisionEssay_el = driver.find_element(By.XPATH, COLLEGE_ADMMISION_ESSAY_XPATH)
random_short_sleep()
collegeAdmmisionEssay_el.click()
random_long_sleep()

# WAIT TILL THE PAGE IS  FULLT LOADED
# assert driver.title == WIZARD_TITLE
print(driver.title)

# Step 1
# Filling title
if not does_element_exist(driver, TITLE_IPNUT_XPATH):
    print("title input element doesn't exist")
title_el = driver.find_element(By.XPATH, TITLE_IPNUT_XPATH)
title_el.click()
random_short_sleep()
enter_text(title_el, cl_title)
random_short_sleep()

# Filling persona
if not does_element_exist(driver, PERSONA_WRITING_FOR_XPATH):
    print("persona input element doesn't exist")
persona_el = driver.find_element(By.XPATH, PERSONA_WRITING_FOR_XPATH)
persona_el.click()
random_short_sleep()
enter_text(persona_el, cl_persona)
random_short_sleep()

# Adding keywords
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
if not does_element_exist(driver, ADD_KEYWORD_BASE_XPATH + "/p"):
        print("keyword input element doesn't exist")
keyword_el = driver.find_element(By.XPATH, ADD_KEYWORD_BASE_XPATH + "/p")
enter_text(keyword_el, cl_keywords[0])
random_short_sleep()
keyword_el.send_keys(Keys.ENTER)
random_short_sleep()
if len(cl_keywords) > 1:
    for i in range(1, len(cl_keywords), 1):
        if not does_element_exist(driver, ADD_KEYWORD_BASE_XPATH + f"[{i}]/p"):
            print("keyword input element doesn't exist")
        keyword_el = driver.find_element(By.XPATH, ADD_KEYWORD_BASE_XPATH + f"[{i}]/p")
        enter_text(keyword_el, cl_keywords[i])
        random_short_sleep()
        keyword_el.send_keys(Keys.ENTER)
        random_short_sleep()

# Generate ouline button
if not does_element_exist(driver, GENERATE_OUTLINE_BUTTON_XPATH):
    print("genrate ouline button doesn't exist")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
generateOutline_el = driver.find_element(By.XPATH, GENERATE_OUTLINE_BUTTON_XPATH)
random_short_sleep()
generateOutline_el.click()
random_long_sleep()

# step 2
# Create points button
if not does_element_exist(driver, CREATE_POINTS_BUTTON_XPATH):
    print("create points doesn't exist")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
random_short_sleep()
createPointsButton_el = driver.find_element(By.XPATH, CREATE_POINTS_BUTTON_XPATH)
random_short_sleep()
createPointsButton_el.click()
random_long_sleep()

# step 3
# finishing up
if not does_element_exist(driver, FINISHING_TOUCHES_BUTTON_XPATH):
    print("finishing touches button doesn't exist")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
random_short_sleep()
finishingButton_el = driver.find_element(By.XPATH, FINISHING_TOUCHES_BUTTON_XPATH)
random_short_sleep()
finishingButton_el.click()
random_long_sleep()

# step 4
# copy
# if not does_element_exist(driver, PUBLISH_MENU_BUTTON_XPATH):
#     print("publish menu button doesn't exist")
# publishMenu_el = driver.find_element(By.XPATH, PUBLISH_MENU_BUTTON_XPATH)
# random_short_sleep()
# publishMenu_el.click()
# random_long_sleep()

# if not does_element_exist(driver, COPY_CONTENT_BUTTON_XPATH):
#     print("publish menu button doesn't exist")
# copyContent_el = driver.find_element(By.XPATH, COPY_CONTENT_BUTTON_XPATH)
# random_short_sleep()
# copyContent_el.click()
# random_long_sleep()

if not does_element_exist(driver, FINAL_CONTENT_XPATH):
    print("publish menu button doesn't exist")
content_el = driver.find_element(By.XPATH, FINAL_CONTENT_XPATH)
random_short_sleep()

all_content_children = content_el.find_elements(By.XPATH, './/*')
print(len(all_content_children))
for el in all_content_children:
    print(el.get_attribute('innerText'))

with open(f"{cl_title}.txt", 'w') as fd:
    for child in all_content_children:
        fd.write(child.get_attribute("innerText"))
        fd.write('\n')


    

