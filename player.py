import random

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
            print(f"-The aircraft was buyed from {self.company} with {aircraft.production_cost}$")
            print(f"-The balance of company {self.company} is {self.cash}$")
            return True
        else:
            print(f"-The company {self.company} does not have the necessary funds to buy aircraft")
            return False

    def sell_aircraft(self, aircraft):
        if aircraft in self.aircrafts:
            self.cash += aircraft.production_cost // 2
            self.aircrafts.remove(aircraft)
            print(f"-The aircraft was selled from {self.company} with {aircraft.production_cost // 2}$")
            print(f"-The balance of company {self.company} is {self.cash}$")
            return True
        else:
            print(f"-The company {self.company} does not have this plane to sell it")
            return False

    def develop_aircraft(self, aircraft):
        cost = random.randint(100000, 1000000)
        aircraft.develop(cost)
        success_rate = random.randint(1, 10)
        print(f"-The aircraft was developed at a cost of {cost}$ and success rate of {success_rate}")
        if success_rate > 5:
            cost_prod = random.randint(100000, 1000000)
            aircraft.produce(cost_prod)
            print(f"-The aircraft have success rate of {success_rate} > 5. will be produced with cost of {aircraft.production_cost}$")
            aircraft.range += random.randint(3000, 9000)
            aircraft.capacity += random.randint(100, 400)
            aircraft.fuel_consumption -= random.randint(1, 5)
            aircraft.speed += random.randint(400, 900)
            print(f"-Information about aircraft, name {aircraft.name}, capacity {aircraft.capacity}, range {aircraft.range}, fuel consumption {aircraft.fuel_consumption}, speed {aircraft.speed}, develpment cost {aircraft.development_cost}, production cost {aircraft.production_cost}.")
        print(f"-The balance of company {self.company} is {self.cash}$")