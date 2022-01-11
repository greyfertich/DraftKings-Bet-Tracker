from table import StatTable

class RushingTable(Table):
    def __init__(self):
        super().__init__()
        self.columns = ["NAME", "CAR", "YDS", "AVG", "TD", "LONG"]
    def add_row(self, data):
        self.rows.append(data)
