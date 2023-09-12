import requests
import pandas as pd


temp_season = ['input 0: 2022-23', 'input 1: 2021-22','input 2: 2020-21']
seasons = ['2022-23', '2021-22', '2020-21'] # -> url list, don't modify

print('select season: {}'.format(temp_season))
print(">>>", end = " ")
input_s = int(input())
s = seasons[input_s]

seasons = ['2022-23', '2021-22', '2020-21'] # -> list can modify

temp_season_types = ['input 0: Regular Season', 'input 1: Pre Season','input 2: Playoffs']
season_types = ['Regular%20Season','Pre+Season','Playoffs'] # -> url list, don't modify

print('select season types: {}'.format(temp_season_types))
print(">>>", end = " ")
input_st = int(input())
st = season_types[input_st]

season_types = ['Regular Season','Pre Season','Playoffs'] # -> list can modify

temp_per_mode = ['input 0: PerGame ', 'input 1: Totals', 'input 2: Per 48 Minutes']
per_mode = ['PerGame ', 'Totals', 'Per48'] # -> url list, don't modify

print('select Mode: {}'.format(temp_per_mode))
print(">>>", end = " ")
input_m = input()
m = per_mode[int(input_m)]

per_mode = ['PerGame ', 'Totals', 'Per 48 Min'] # -> list can modify

url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=" + m + "&Scope=S&Season=" + s + "&SeasonType=" + st + "&StatCategory=PTS"

headers = {
    'authority': 'stats.nba.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.nba.com',
    'referer': 'https://www.nba.com/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers).json()

categories = response['resultSet']['headers']

playerData = response['resultSet']['rowSet']

index = []

size = len(playerData)

for i in range(size + 1):
    index.append(i)
index.pop(0)

temp_df1 = pd.DataFrame(playerData, columns=categories, index=index)
temp_df1 = temp_df1.drop("TEAM_ID", axis=1)

temp_df2 = pd.DataFrame({
    "SEASON": [s  for i in range(size)],
    "SEASON TYPE": [st  for i in range(size)],
    "PER MODE": [m  for i in range(size)],
    "STAT CATEGORY": ['PTS' for i in range(size)]
}, index=index)

df = pd.concat([temp_df2, temp_df1], axis=1)

df.to_excel('playerdata_dynamic.xlsx')
