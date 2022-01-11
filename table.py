class StatTable:
    def __init__(self):
        self.home_rows = []
        self.away_rows = []
    def add_home_row(self, data):
        self.home_rows.append(data)
    def add_away_row(self, data):
        self.away_rows.append(data)

class RushingTable(StatTable):
    def __init__(self):
        super().__init__()
        self.columns = ["NAME", "CAR", "YDS", "AVG", "TD", "LONG"]

class ReceivingTable(StatTable):
    def __init__(self):
        super().__init__()
        self.columns = ["REC", "YDS", "AVG", "TD", "LONG", "TGTS"]

class PassingTable(StatTable):
    def __init__(self):
        super().__init__()
        self.columns = ["C/ATT", "YDS", "AVG", "TD", "INT", "SACKS", "QBR", "RTG"]

class FumbleTable(StatTable):
    def __init__(self):
        super().__init__()
        self.columns = ["FUM", "LOST", "REC"]

class DefensiveTable(StatTable):
    def __init__(self):
        super().__init__()
        self.columns = ["TOT", "SOLO", "SACKS", "TFL", "PD", "QB HITS", "TD"]
