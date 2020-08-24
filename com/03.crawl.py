from selenium import webdriver
from time import sleep
import requests
from bs4 import BeautifulSoup
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

driver = webdriver.Chrome('../chromedriver.exe')
driver.implicitly_wait(3)
url='https://www.instagram.com/accounts/login/'
driver.get(url) #enter

# soup = BeautifulSoup(data.text, 'html.parser')

sleep(5)
driver.find_element_by_name('username').send_keys('01050083203')
driver.find_element_by_name('password').send_keys('eogkrtod12')

sleep(3)
# 로그인버튼 누르기
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
# 버튼누르기
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
# 버튼 누르기
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
sleep(3)
driver.get('https://www.instagram.com/explore/tags/수원돈까스맛집')
sleep(3)

pageString=driver.page_source

print(pageString)


# driver.close()