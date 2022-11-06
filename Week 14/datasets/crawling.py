from selenium import webdriver
import sqlite3
# from webdriver_manager import driver
# from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
import time

db = sqlite3.connect('hospitals')
cursor = db.cursor()


# base_url = 'https://www.drsaina.com/hospital?pageIndex=1'
base_url = 'https://kilid.com/buy/tehran-satarkhan?listingTypeId=1&location=328363&page=0&sort=DATE_DESC'

ch = webdriver.Chrome(ChromeDriverManager().install())

ch.get(base_url)

info = ch.find_elements_by_xpath("//app-listinlist-view-card/a/div/div[2]/div[1]")
for elem in info:
    print(elem.text)

agencies = ch.find_elements_by_class_name("agency-container")
for agency in agencies:
    print(agency.text)

ad_id = list()
urls = [elem.get_attribute("href") for elem in ch.find_elements_by_xpath("//app-listing-list-view-card/a")]
for url in urls:
    print(url)
    ad_id.append(int(url.split('/')[-1]))

for url in urls:
    ch.maximize_window()
    ch.get(url)
    ch.find_element(By.CLASS_NAME, 'single-sticky__button--call').click()
    # ch.implicitly_wait(1)
    time.sleep(2)
    facilities = ch.find_elements_by_class_name("single-data__container--attributes")
    for f in facilities:
        print(f.text)
    print('-----------')
    features = ch.find_elements(By.CLASS_NAME, "single-feature__type")
    for f in features:
        print(f.text)
    print('-----------')
    description = ch.find_elements(By.CLASS_NAME, "single-description")
    for d in description:
        print(d.text)
    print('-----------')
    agent_info = ch.find_elements(By.CLASS_NAME, "single-sticky__department__contact-info")
    for d in agent_info:
        print(d.text)
    phone = ch.find_elements(By.XPATH, "//button/p")
    for p in phone:
        print(p.text)
    print('=' * 40)


print(ad_id)
print(len(ad_id))


# driver.find_elements(By.XPATH, '//button')
# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")

