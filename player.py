class Player:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def buy_aircraft(self, aircraft):
        aircraft.develop(1000);
        print("player buying aircraft")

    def sell_aircraft(self, aircraft):
        print("player selling aircraft")
