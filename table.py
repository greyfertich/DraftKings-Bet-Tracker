from constants import *

class StatTable(object):
    def __init__(self):
        self.home_rows = []
        self.away_rows = []
        self.type = "Default"

    def createTable(self, id):
        if id == PASSING_ID:
            return PassingTable()
        elif id == RUSHING_ID:
            return RushingTable()
        elif id == RECEIVING_ID:
            return ReceivingTable()
        elif id == FUMBLE_ID:
            return FumbleTable()
        elif id == DEFENSIVE_ID:
            return DefensiveTable()
        elif id == INTERCEPTION_ID:
            return InterceptionTable()
        elif id == KICKRETURN_ID:
            return KickReturnTable()
        elif id == PUNTRETURN_ID:
            return PuntReturnTable()
        elif id == KICKING_ID:
            return KickingTable()
        elif id == PUNTING_ID:
            return PuntingTable()

    def add_home_row(self, data):
        self.home_rows.append(data)

    def add_away_row(self, data):
        self.away_rows.append(data)

    def add_empty_home_row(self):
        self.home_rows.append("No " + self.type + " Data Available.")

    def add_empty_away_row(self):
        self.away_rows.append("No " + self.type + " Data Available.")

class RushingTable(StatTable):
    def __init__(self):
        super(RushingTable, self).__init__()
        self.attributes = ["name", "car", "yds", "avg", "td", "long"]
        self.type = "Rushing"

class ReceivingTable(StatTable):
    def __init__(self):
        super(ReceivingTable, self).__init__()
        self.attributes = ["rec", "yds", "avg", "td", "long", "tgts"]
        self.type = "Receiving"

class PassingTable(StatTable):
    def __init__(self):
        super(PassingTable, self).__init__()
        self.attributes = ["c-att", "yds", "avg", "td", "int", "sacks", "qbr", "rtg"]
        self.type = "Passing"

class FumbleTable(StatTable):
    def __init__(self):
        super(FumbleTable, self).__init__()
        self.attributes = ["fum", "lost", "rec"]
        self.type = "Fumble"

class DefensiveTable(StatTable):
    def __init__(self):
        super(DefensiveTable, self).__init__()
        self.attributes = ["tot", "solo", "sacks", "tfl", "pd", "qb hts", "td"]
        self.type = "Defensive"

class InterceptionTable(StatTable):
    def __init__(self):
        super(InterceptionTable, self).__init__()
        self.attributes = ["int", "yds", "td"]
        self.type = "Interception"

class KickReturnTable(StatTable):
    def __init__(self):
        super(KickReturnTable, self).__init__()
        self.attributes = ["no", "yds", "avg", "long", "td"]
        self.type = "Kick Return"

class PuntReturnTable(StatTable):
    def __init__(self):
        super(PuntReturnTable, self).__init__()
        self.attributes = ["no", "yds", "avg", "long", "td"]
        self.type = "Punt Return"

class KickingTable(StatTable):
    def __init__(self):
        super(KickingTable, self).__init__()
        self.attributes = ["fg", "pct", "long", "xp", "pts"]
        self.type = "Kicking"

class PuntingTable(StatTable):
    def __init__(self):
        super(PuntingTable, self).__init__()
        self.attributes = ["no", "yds", "avg", "tb", "in 20", "long"]
        self.type = "Punting"
