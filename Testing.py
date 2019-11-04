
#imports
from selenium import webdriver
import bs4 as bs 
import urllib.request


url = 'https://www.oddschecker.com/au/australian-rules'

#before headers 
response=requests.get(url)
print(response)

#add headers to bypass 403 error
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers={'User-Agent': user_agent}

#after header
response=requests.get(url, headers=headers)
##html=response.content
print(response)


driver = webdriver.Chrome('/Users/karthus/Desktop/chromedriver 3')
driver.get(url)
html = driver.page_source


#Use BeautifulSoup
sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce,'lxml')
#print(soup.find_all('class'))


#close browser instance
driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




