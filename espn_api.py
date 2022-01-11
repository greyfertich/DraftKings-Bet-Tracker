import requests
from bs4 import BeautifulSoup
from rushingtable import RushingTable

class Espn_api:
    global url_prefix
    url_prefix = "https://www.espn.com/nfl/boxscore/_/gameId/"
    @classmethod
    def get_team_stats(cls, game_id):
        print(game_id)
        team_stats_response = requests.get(url_prefix + str(game_id))
        print(url_prefix + str(game_id))
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
        away_data_table = away_data.find("table", class_="mod-data").find("tbody")
        away_data_table_rows = set(away_data_table.find_all("tr")).difference(away_data_table.find_all("tr", class_="highlight"))

        home_data = rushing_data.find("div", class_="gamepackage-home-wrap")
        home_data_table = home_data.find("table", class_="mod-data").find("tbody")
        home_data_table_rows  = set(home_data_table.find_all("tr")).difference(home_data_table.find_all("tr", class_="highlight"))

        away_table = RushingTable()
        home_table = RushingTable()

        for row in away_data_table_rows:
            name_data = row.find("td", class_="name")
            name = next(iter(set(name_data.find_all("span")).difference(name_data.find_all("span", class_="abbr")))).text
            carries = row.find("td", class_="car").text
            yards = row.find("td", class_="yds").text
            average = row.find("td", class_="avg").text
            touchdowns = row.find("td", class_="td").text
            long = row.find("td", class_="long").text
            away_table.add_row([name, carries, yards, average, touchdowns, long])

        for row in home_data_table_rows:
            name_data = row.find("td", class_="name")
            name = next(iter(set(name_data.find_all("span")).difference(name_data.find_all("span", class_="abbr")))).text
            carries = row.find("td", class_="car").text
            yards = row.find("td", class_="yds").text
            average = row.find("td", class_="avg").text
            touchdowns = row.find("td", class_="td").text
            long = row.find("td", class_="long").text
            home_table.add_row([name, carries, yards, average, touchdowns, long])

        for row in home_table.rows:
            print(row)

        for row in away_table.rows:
            print(row)




Espn_api.get_team_stats(401326595)
