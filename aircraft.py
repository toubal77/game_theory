import random

class Aircraft:
    def __init__(self, name, capacity, range, fuel_consumption, speed):
        self.name = name
        self.capacity = capacity
        self.range = range
        self.fuel_consumption = fuel_consumption
        self.speed = speed
        self.development_cost = 0
        self.production_cost = 0

    def develop(self, cost):
        self.development_cost += cost

    def produce(self, cost):
        self.production_cost += cost

    def develop_aircraft(aircraft):
        cost = random.randint(100000, 1000000)
        aircraft.develop(cost)
        success_rate = random.randint(1, 10)
        if success_rate > 5:
            aircraft.range += random.randint(1000, 5000)
            aircraft.capacity += random.randint(10, 100)
            aircraft.fuel_consumption -= random.randint(1, 5)
            aircraft.speed += random.randint(50, 200)

    def is_competitive(self, competitor):
        if self.capacity > competitor.capacity and self.range > competitor.range and \
           self.fuel_consumption < competitor.fuel_consumption and self.speed > competitor.speed:
            return True
        else:
            return False
