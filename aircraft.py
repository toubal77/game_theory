class Aircraft:
    def __init__(self, name, capacity, range, fuel_consumption, speed, production_cost):
        self.name = name
        self.capacity = capacity
        self.range = range
        self.fuel_consumption = fuel_consumption
        self.speed = speed
        self.development_cost = 0
        self.production_cost = production_cost

    def develop(self, cost):
        self.development_cost += cost

    def produce(self, cost):
        self.production_cost += cost


    def is_competitive(self, competitor):
        if self.capacity > competitor.capacity and self.range > competitor.range and \
           self.fuel_consumption < competitor.fuel_consumption and self.speed > competitor.speed:
            print("-The aircraft was competitive")
            return True
        else:
            print("-The competitor was competitive")
            return False
