class Player:
    def __init__(self, name, company):
        self.name = name
        self.company = company
        self.cash = 1000000
        self.aircrafts = []

    def buy_aircraft(self, aircraft):
        if self.cash >= aircraft.production_cost:
            self.cash -= aircraft.production_cost
            self.aircrafts.append(aircraft)
            return True
        else:
            return False

    def sell_aircraft(self, aircraft):
        if aircraft in self.aircrafts:
            self.cash += aircraft.production_cost // 2
            self.aircrafts.remove(aircraft)
            return True
        else:
            return False
