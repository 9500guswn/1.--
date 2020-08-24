from my_project.libs.crawler import crawl

url='https://www.instagram.com/accounts/login/'
pageString=crawl(url)
print(pageString)