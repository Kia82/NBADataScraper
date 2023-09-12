import requests
import pandas as pd

url = "https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2022-23&SeasonType=Regular%20Season&StatCategory=PTS"


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
        "SEASON": ['2022-23' for i in range(size)],
        "SEASON TYPE": ['Regular' for i in range(size)],
        "PER MODE": ['Per Game' for i in range(size)],
        "STAT CATEGORY": ['PTS' for i in range(size)]
    }, index=index)

df = pd.concat([temp_df2, temp_df1], axis=1)

df.to_excel('playerdata_static.xlsx')


