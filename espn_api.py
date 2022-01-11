import requests
from bs4 import BeautifulSoup

class Espn_api:
    global url_prefix
    url_prefix = "https://www.espn.com/nfl/boxscore/_/gameId/"
    @classmethod
    def get_team_stats(cls, game_id):
        team_stats_response = requests.get(url_prefix + str(game_id))
        team_stats_soup = BeautifulSoup(team_stats_response.text, 'html.parser')
        tables = team_stats_soup.find_all("table", class_="mod-data")
        table_data = [cls.get_table_data(table) for table in tables[:1]]
    @classmethod
    def get_table_data(cls, table):
        tds = table.find_all("td")
        for td in tds:
            print(td)
            print()

Espn_api.get_team_stats(401326600)
