
# %%
from selenium import webdriver
import sqlite3
# from webdriver_manager import driver
# from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
import time
import datetime

# %%
db = sqlite3.connect('housing_information')
cursor = db.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS details (record_id INTEGER, ad_id INTEGER, ad_url TEXT, '
               'title TEXT, price TEXT, ppsm TEXT, location TEXT, building_type TEXT, '
               'building_area TEXT, bedrooms TEXT, construction_year INTEGER, parking TEXT, facilities TEXT, '
               'description TEXT, agency_info TEXT, agent_phone TEXT)')


base_url = 'https://kilid.com/buy/tehran-satarkhan?listingTypeId=1&location=328363&page=0&sort=DATE_DESC'

ch = webdriver.Chrome(ChromeDriverManager().install())
ch.maximize_window()
ch.get(base_url)

title = list()
price = list()
ppsm = list()
location = list()
building_type = list()
# building_area
# bedrooms
# construction_year
# parking
# facilities
# description
# agency_info

# record = list()


ad_id = list()
record_id = 1 + len(ad_id)
urls = [elem.get_attribute("href") for elem in ch.find_elements_by_xpath("//app-listing-list-view-card/a")]
for url in urls:
    # print(url)
    ad_id.append(int(url.split('/')[-1]))


info = ch.find_elements_by_xpath("//app-listing-list-view-card/a/div/div[2]/div[1]")
for elem in info:
    # print(elem.text)
    items = elem.text.split('\n')
    title.append(items[0])
    no_price_flag = False
    no_ppsm_flag = False
    for i in items:
        if 'قیمت:' in i:
            price.append(i.strip('قیمت:'))
            break
    else:
        price.append('قیمتی وارد نشده')
        no_price_flag = True

    for i in items:
        if 'مربع:' in i:
            ppsm.append(i.strip('قیمت هر متر مربع:'))
            break
    else:
        ppsm.append('قیمتی وارد نشده')
        no_ppsm_flag = True

    if no_price_flag:
        items.insert(1, None)
    if no_ppsm_flag:
        items.insert(2, None)

    location.append(items[3])
    building_type.append(items[4])

# agencies = ch.find_elements_by_class_name("agency-container")
# for agency in agencies:
#     print(agency.text)


for ind, url in enumerate(urls):
    record = list()
    record.append(record_id)
    record.append(ad_id[ind])
    record.append(url)
    record.append(title[ind])
    record.append(price[ind])
    record.append(ppsm[ind])
    record.append(location[ind])
    record.append(building_type[ind])

    cursor.execute('INSERT INTO details (record_id) VALUES ({})'.format(record_id))
    cursor.execute('UPDATE details SET ad_id={} WHERE record_id={}'.format(ad_id[ind], record_id))
    cursor.execute('UPDATE details SET ad_url="{}" WHERE record_id={}'.format(url, record_id))
    cursor.execute('UPDATE details SET title="{}" WHERE record_id={}'.format(title[ind], record_id))
    cursor.execute('UPDATE details SET price="{}" WHERE record_id={}'.format(price[ind], record_id))
    cursor.execute('UPDATE details SET ppsm="{}" WHERE record_id={}'.format(ppsm[ind], record_id))
    cursor.execute('UPDATE details SET location="{}" WHERE record_id={}'.format(location[ind], record_id))
    cursor.execute('UPDATE details SET building_type="{}" WHERE record_id={}'.format(building_type[ind], record_id))

    ch.get(url)
    ch.find_element(By.CLASS_NAME, 'single-sticky__button--call').click()
    # ch.implicitly_wait(1)
    time.sleep(2)

    facilities = ch.find_elements_by_class_name("single-data__container--attributes")
    items = facilities[0].text.split('\n')
    for i in items:
        if 'متر' in i:
            record.append(i.strip(' متر'))
            temp = i.strip(' متر')
            break
    else:
        record.append('قید نشده')
        temp = 'قید نشده'
    cursor.execute('UPDATE details SET building_area="{}" WHERE record_id={}'.format(temp, record_id))

    for i in items:
        if 'خوابه' in i:
            record.append(i.strip(' خوابه'))
            temp = i.strip(' خوابه')
            break
    else:
        record.append('قید نشده')
        temp = 'قید نشده'
    cursor.execute('UPDATE details SET bedrooms="{}" WHERE record_id={}'.format(temp, record_id))

    for i in items:
        if 'ساله' in i:
            record.append(datetime.datetime.today().year - int(i.strip(' ساله')))
            temp = datetime.datetime.today().year - int(i.strip(' ساله'))
            break
    else:
        record.append('قید نشده')
        temp = -1
    cursor.execute('UPDATE details SET construction_year={} WHERE record_id={}'.format(temp, record_id))

    for i in items:
        if 'پارکینگ' in i:
            record.append(i.strip(' پارکینگ'))
            temp = i.strip(' پارکینگ')
            break
    else:
        record.append('قید نشده')
        temp = 'قید نشده'
    cursor.execute('UPDATE details SET parking="{}" WHERE record_id={}'.format(temp, record_id))

    # print('-----------')
    features = ch.find_elements(By.CLASS_NAME, "single-feature__type")
    items = features[0].text.split('\n')
    if items:
        record.append(tuple(items))
        temp = ','.join(items)
    else:
        record.append('قید نشده')
        temp = 'قید نشده'
    cursor.execute('UPDATE details SET facilities="{}" WHERE record_id={}'.format(temp, record_id))

    # print('-----------')
    description = ch.find_elements(By.CLASS_NAME, "single-description")
    items = description[0].text.split('\n')
    items = tuple(filter(lambda a: a != '', items))
    if items:
        record.append(items)
        temp = ','.join(items)
    else:
        record.append('قید نشده')
        temp = 'قید نشده'
    cursor.execute('UPDATE details SET description="{}" WHERE record_id={}'.format(temp, record_id))

    # print('-----------')
    agent_info = ch.find_elements(By.CLASS_NAME, "single-sticky__department__contact-info")
    items = agent_info[0].text.split('\n')
    if items:
        record.append(tuple(items))
        temp = ','.join(items)
    else:
        record.append('قید نشده')
        temp = 'قید نشده'
    cursor.execute('UPDATE details SET agency_info="{}" WHERE record_id={}'.format(temp, record_id))

    phone = ch.find_elements(By.XPATH, "//button/p")
    if phone[0].text:
        record.append(phone[0].text)
        temp = phone[0].text
    else:
        record.append('قید نشده')
        temp = 'قید نشده'
    cursor.execute('UPDATE details SET agent_phone="{}" WHERE record_id={}'.format(temp, record_id))

    print(record)

    print('=' * 40)

    record_id += 1
    db.commit()


cursor.close()
db.close()

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

