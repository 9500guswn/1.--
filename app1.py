from selenium import webdriver
import time
import warnings
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.project
import lxml
# from lxml import etree
import re
driver = webdriver.Chrome('chromedriver.exe')
# 3초 기다리는 함수(implicitly_wait)
driver.implicitly_wait(3)
# 경고메시지 제거 패키지
warnings.filterwarnings(action='ignore')

def get_content(driver):
    html=driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # soup=BeautifulSoup(html,lxml)
    # print(soup)
    # reviews=soup.select('div.EZdmt > div > div > div')
    # # body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > div > li > div > div > div.C4VMK > span
    # # tag_list=[]
    # for tags in reviews:
    #     hashtag=tags.select_one('a > div > div > img')['src']
    #     # body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > div > li > div > div > div.C4VMK > span > a: nth - child(
    #     #     # 10)
    #     print(hashtag)
    for i in soup.find_all("a", class_="xil3i") :
        print(i.text[1:])
        pageString = driver.page_source
        print(pageString)

    # try:
    #
    #     content=soup.select('div.C4VMK > span')[0].text
    # except:
    #     content = ' '
    #     tags = re.findall(r'#[^\s#,\\]+', content)  #
driver.get('https://www.instagram.com/accounts/login/')

time.sleep(3)

# driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("01050083203")
# driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("eogkrtod12")
driver.find_element_by_name('username').send_keys('01050083203')
driver.find_element_by_name('password').send_keys('eogkrtod12')

time.sleep(3)
# 로그인버튼 누르기
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
# 버튼누르기
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
# 버튼 누르기
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
time.sleep(3)
driver.get('https://www.instagram.com/explore/tags/수원돈까스맛집')
time.sleep(3)
# 일치하는 CSS 선택자가있는 첫 번째 요소가 반환됩니다.
first=driver.find_element_by_css_selector ( "div._9AhH0")
first.click()
time.sleep(3)
result=[]
target=10

