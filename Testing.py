from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.oddschecker.com/au/australian-rules'

driver = webdriver.Chrome('/Users/karthus/Desktop/chromedriver 3')
driver.get(url)
html = driver.page_source

#BeautifulSoup grab html
soup = BeautifulSoup(html, 'lxml')

#initialisation
date_list, time_list, odds_list = [], [], []
home_odds_list, away_odds_list = [], []
team_list, home_team_list, away_team_list = [], [], []
url_list=[]

#Dictionary for tags
tag = {
    "games" : "_2nWFsl",
    "date"  : "_1svvs0",
    "time"  : "_1ob6_g",
    "odds"  : "_1NtPy1",
    "teams" : "_2tehgH", 
    "urls"  : "_119e1b",
}

#For a game match
def parse_games(game_day, game_time_list, game_team_list, game_odds_list,game_url_list):
    """Parse all the lists into a list with each tuple storing the game information"""
    game_list = [] # for storing all games
    
    def split_list(alist):
        """Split a list into two lists with odd/even indices"""
        return alist[0:][::2], alist[1:][::2]
    
    home_team_list, away_team_list = split_list(game_team_list)
    home_odds_list, away_odds_list = split_list(game_odds_list)
    
    for time, home_team, away_team, home_odds, away_odds,url in zip(game_time_list, home_team_list, away_team_list,home_odds_list, away_odds_list,game_url_list):
    
        record = (game_day, time, home_team, away_team, home_odds, away_odds,url)
        game_list.append(record)
    return game_list

#for all game matches
all_games_list = []


# Start 
for game in soup.find_all("div", class_=tag['games']):
    # for each game, we will store it's information into the game_list
    game_time_list, game_odds_list, game_team_list = [], [], []
    game_url_list=[]
    for date in game.findAll("div", class_ = tag['date']):
        game_day = date.text
    for time in game.findAll("div", class_ = tag['time']):
        game_time_list.append(time.text)
    for teams in game.findAll("div", class_ = tag['teams']):
        game_team_list.append(teams.text)
    for odds in game.findAll("div", class_ = tag['odds']):
        game_odds_list.append(odds.text)
    for urls in game.findAll("a", class_= tag['urls']):
        game_url_list.append(urls.get('href'))

    game_list = parse_games(game_day, game_time_list, game_odds_list, game_team_list,game_url_list)
    all_games_list.append(game_list)
    
    
#print(game_url_list)
#print(all_games_list)
flat_games_list = [item for sublist in all_games_list for item in sublist]
print(flat_games_list)

df = pd.DataFrame(flat_games_list)

df.columns = ["date", "time", "home_odds", "away_odds", "home", "away","urls"]
pd.set_option('max_colwidth', 1000)
display(df)
