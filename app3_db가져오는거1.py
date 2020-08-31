from selenium import webdriver
import time
import warnings
from bs4 import BeautifulSoup
from pymongo import MongoClient
import re# pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.project
driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(3)
warnings.filterwarnings(action='ignore')
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
# for i in soup.find_all("a", class_="xil3i") :
#     print(i.text[1:])
#     pageString = driver.page_source
#     print(pageString)

# try:
#
#     content=soup.select('div.C4VMK > span')[0].text
# except:
#     content = ' '
#     tags = re.findall(r'#[^\s#,\\]+', content)  #
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

# date=driver.get('https://www.instagram.com/explore/tags/수원돈까스맛집')
# soup = BeautifulSoup(date, 'html.parser')
driver.get('https://www.instagram.com/explore/tags/수원돈까스맛집')
instagram_tags = []
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# one=soup.select()
time.sleep(3)

opening = driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w') # 맨 첫번째 게시물 클릭
opening.click()

time.sleep(3)

# for i in range(100):
#     time.sleep(2)
#     data = driver.find_element_by_css_selector('.C7I1f.X7jCj')# C7I1f X7jCj 해시태그값 가져오기
#     if data is None:
#         continue
#     tag_raw = data.text
#     tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
#     tag = ''.join(tags).replace("#", " ")
#     tag_data = tag.split()
#     next = driver.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow") # 다음 게시물로 넘어가기 클릭
#     next.click()
#     print(tag_data)
#     db.foodList.insert_one({
#         'tag':tag_data,
#         'local' : '수원',
#         'food' : '파스타'
#     })
for i in range(100):
    time.sleep(2)
    data = driver.find_element_by_css_selector('.C7I1f.X7jCj,.eo2As')# 해시태크값 가져오기
    # data가 없는 경우 다음으로 넘어가기
    if data is None:
        continue
    tag_raw = data.text
    tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
    tag = ''.join(tags).replace("#", " ")
    if tag is None:
        continue
    tag_data = tag.split()
    next = driver.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow") # 다음 게시물로 넘어가기 클릭
    next.click()
    print(tag_data)
    db.수원맛집.insert_one({
        'tag':tag_data,
        'local' : '수원',
        'food' : '돈까스맛집'
    })
    # print(tag_data)
    # for tag in tags:
    #     tag = tags.text.strip()
    #     print(tag)


        # for post in opening:
        #     posts=


# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# tags = soup.select('.xil3i')
# print(tags)
# print(type(insta))
# for opening in tags:
#     opening = driver.find_element_by_css_selector("div._9AhH0")
#     opening.click()
#     time.sleep(3)
#
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#     tags = soup.select('.xil3i')
#
#     for tag in tags:
#     # print(tag)
#     open = tag.text
#     db.project.insert_one({
#         'open': open
#     })
#     closing = driver.find_element_by_css_selector("div._8-yf5")
#     closing.click()
    # driver.close()
    # tag=i.select_one('span > a')
    # tag=i.select_one(".xil3i")
    # print(tag)
    # p