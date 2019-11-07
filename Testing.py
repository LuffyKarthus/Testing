from selenium import webdriver
from bs4 import BeautifulSoup

import pandas as pd

url = 'https://www.oddschecker.com/au/australian-rules'
driver = webdriver.Chrome('/Users/karthus/Desktop/chromedriver 3')
driver.get(url)
html = driver.page_source

#BeautifulSoup grab html
soup = BeautifulSoup(html, 'lxml')

Bet_list=[]
Home_odds_list=[]
Away_odds_list=[]

Team_list=[]
Home_team_list=[]
Away_team_list=[]

Date_list=[]
Time_list=[]

#counter set to 0
i=0;
j=0;
#enable viewing how tags are nested in the document
#soup.prettify()

for bet in soup.find_all("div", class_="_1NtPy1"):
    Bet_list.append(bet.text)

for bet in Bet_list:
    if (i%2==0):
        Home_odds_list.append(bet)       
    else:
        Away_odds_list.append(bet)
    i=i+1
    
for Team in soup.find_all("div", class_="_2tehgH"):
    Team_list.append(Team.text)
    
for Team in Team_list:
    if (j%2==0):
        Home_team_list.append(Team)
    else:
        Away_team_list.append(Team)
    j=j+1

for Date in soup.find_all("div", class_="_1svvs0"):
    Date_list.append(Date.text)
for Time in soup.find_all("div", class_="_1ob6_g"):
    Time_list.append(Time.text)
    
    
print(Home_odds_list)
print(Away_odds_list)
print(Home_team_list)
print(Away_team_list)


#df=pd.DataFrame({'Home_team':Home_team_list})
#print(df)


Date_list=[]
Time_list=[]

