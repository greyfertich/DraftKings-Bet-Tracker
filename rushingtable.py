from table import StatTable

class RushingTable(Table):
    def __init__(self):
        super().__init__()
        self.columns = ["NAME", "CAR", "YDS", "AVG", "TD", "LONG"]
    def add_home_row(self, data):
        self.home_rows.append(data)
    def add_away_row(self, data):
        self.away_rows.append(data)
