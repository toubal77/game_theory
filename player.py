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
            print(f"The aircraft was buyed from {self.company} with {aircraft.production_cost}$")
            return True
        else:
            print(f"The company {self.company} does not have the necessary funds")
            return False

    def sell_aircraft(self, aircraft):
        if aircraft in self.aircrafts:
            self.cash += aircraft.production_cost // 2
            self.aircrafts.remove(aircraft)
            print(f"The aircraft was selled from {self.company} with {aircraft.production_cost // 2}$")
            return True
        else:
            print(f"The company {self.company} does not have this plane")
            return False
