from selenium import webdriver
import time
import warnings
from pymongo import MongoClient
import re

client = MongoClient('localhost', 27017)
db = client.project
driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(3)
warnings.filterwarnings(action='ignore')

driver.get('https://www.instagram.com/accounts/login/')

time.sleep(3)

driver.find_element_by_name('username').send_keys('01050083203')
driver.find_element_by_name('password').send_keys('eogkrtod12')

time.sleep(3)
# 로그인버튼 누르기
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
# 버튼누르기
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
# 버튼 누르기
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
time.sleep(3)

driver.get('https://www.instagram.com/explore/tags/수원돈까스맛집')
instagram_tags = []

time.sleep(3)

opening = driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w')
opening.click()

time.sleep(3)

for i in range(3):
    time.sleep(2)

    data = driver.find_element_by_css_selector('.C7I1f.X7jCj')
    tag_raw = data.text
    tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
    tag = ''.join(tags).replace("#", " ")
    tag_data = tag.split()

    next = driver.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow")
    next.click()
    print(tag_data)
    db.my_project.insert_one({
        'tag':tag_data,
    })