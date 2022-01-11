import requests
from bs4 import BeautifulSoup

class Espn_api:
    global url_prefix
    url_prefix = "https://www.espn.com/nfl/boxscore/_/gameId/"
    @classmethod
    def get_team_stats(cls, game_id):
        print(game_id)
        team_stats_response = requests.get(url_prefix + str(game_id))
        team_stats_soup = BeautifulSoup(team_stats_response.text, 'html.parser')
        # tables = team_stats_soup.find_all("table", class_="mod-data")
        # table_data = [cls.get_table_data(table) for table in tables]
        table_data = cls.get_rushing_data(team_stats_soup)
        # for table in table_data:
        #     print(table)
    @classmethod
    def get_table_data(cls, table):
        tds = table.find_all("td")
        data = {}
        try:
            player_name = next(iter(set(tds[0].find_all("span")).difference(tds[0].find_all("span", class_="abbr")))).text
            print(player_name)
            for td in tds[1:]:
                data[td['class'][0]] = td.text
        except Exception as e:
            player_name = "INVALID_NAME"
        return player_name, data
    @classmethod
    def get_rushing_data(cls, soup):
        rushing_data = soup.find("div", {"id":"gamepackage-rushing"})
        away_data = rushing_data.find("div", class_="gamepackage-away-wrap")
        print(away_data)

Espn_api.get_team_stats(401326600)
