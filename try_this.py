from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.oddschecker.com/au/australian-rules'
driver = webdriver.Chrome('/Users/karthus/Desktop/chromedriver 3')
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
soup.findAll('p', {"class":"meeting__name"})
