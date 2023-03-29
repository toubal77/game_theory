import random


class Cooperation:
    def __init__(self, cash):
        self.cash = cash
        self.cost = 0
        self.cost_prod = 0

    def develop_aircraft(self, aircraft, player1, player2):
        print(f"-The balance of cooperation {self.cash}")
        cost = random.randint(100000, 1000000)
        if self.cash >= cost:
            player1.get_cash_before_cooperation()
            player2.get_cash_before_cooperation()
            self.cash -= cost
            self.cost = cost
            success_rate = random.randint(1, 10)
            print(f"-The aircraft was developed at a cost of {cost}$ and success rate of {success_rate}")
            print(f"-The balance of cooperation {self.cash} after develop aircraft is {self.cost}$")
            if success_rate > 5:
                cost_prod = random.randint(100000, 1000000)
                if self.cash >= cost_prod:
                    self.cash -= cost_prod
                    self.cost_prod = cost_prod
                    print(f"-The balance of cooperation {self.cash} after produce is {self.cost_prod}$")
                    print(f"-The aircraft have success rate of {success_rate} > 5. will be produced with "
                          f"cost of {cost_prod}$")
                    aircraft.range += random.randint(3000, 9000)
                    aircraft.capacity += random.randint(100, 400)
                    aircraft.fuel_consumption -= random.randint(1, 5)
                    aircraft.speed += random.randint(400, 900)
                    print(
                        f"-Information about aircraft, name {aircraft.name}, capacity {aircraft.capacity},"
                        f" range {aircraft.range}, fuel consumption {aircraft.fuel_consumption}, "
                        f"speed {aircraft.speed},"
                        f" development cost {aircraft.development_cost}, production cost {aircraft.production_cost}.")
                    player1.get_aircraft_cooperation(aircraft)
                    player2.get_aircraft_cooperation(aircraft)
                else:
                    print(
                        f"-The cooperation does not have the necessary funds to produce "
                        f"aircraft {self.cash}$, cost of produce is {cost_prod}$")
            player1.get_cash_after_cooperation(self.cash // 2)
            player2.get_cash_after_cooperation(self.cash // 2)
        else:
            print(
                f"-The cooperation does not have the necessary funds to develop "
                f"aircraft {self.cash}$, cost of develop is {cost}$")