from table import StatTable

class RushingTable(Table):
    def __init__(self):
        super().__init__()
        self.columns = ["REC", "YDS", "AVG", "TD", "LONG", "TGTS"]
    def add_row(self, data):
        self.rows.append(data)
