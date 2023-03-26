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