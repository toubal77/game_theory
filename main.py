import aircraft
import player

if __name__ == '__main__':
    boeing_airlines = aircraft.Aircraft("Boeing", 0, 0, 0, 0)
    airbus_airlines = aircraft.Aircraft("Airbus", 0, 0, 0, 0)
    player_airAlgerie = player.Player("Algerie", "Air algerie")
    player_airFrance = player.Player("France", "Air france")

    player_airFrance.buy_aircraft(boeing_airlines)
    player_airFrance.buy_aircraft(airbus_airlines)
    player_airFrance.sell_aircraft(boeing_airlines)
    player_airFrance.sell_aircraft(airbus_airlines)
