import aircraft
import player
import cooperation
import random
if __name__ == '__main__':
    #it is planes already produced and developed ready to be sold
    boeing1 = aircraft.Aircraft("737", 160, 5560, 3, 550, 425265, False)
    airbus1 = aircraft.Aircraft("A330", 320, 7500, 3, 720, 592500, True)
    boeing2 = aircraft.Aircraft("777", 380, 9000, 4, 800, 654800, False)
    airbus2 = aircraft.Aircraft("A380", 400, 9000, 4, 850, 721502, True)
    boeing3 = aircraft.Aircraft("764", 250, 6253, 2, 628, 356852, False)
    airbus3 = aircraft.Aircraft("A310", 110, 5800, 2, 525, 285647, True)
    boeing4 = aircraft.Aircraft("737", 160, 5560, 3, 550, 425265, False)
    airbus4 = aircraft.Aircraft("A330", 320, 7500, 3, 720, 592500, True)
    boeing5 = aircraft.Aircraft("777", 380, 9000, 4, 800, 654800, False)
    airbus5 = aircraft.Aircraft("A380", 400, 9000, 4, 850, 721502, True)
    boeing6 = aircraft.Aircraft("764", 250, 6253, 2, 628, 356852, False)
    airbus6 = aircraft.Aircraft("A310", 110, 5800, 2, 525, 285647, True)
    #player statement
    toubal = player.Player("Toubal", "Boeing")
    oualladi = player.Player("Oualladi", "Airbus")
    # Demander aux joueurs d'acheter ou de vendre des avions
        # choice if company toubal want to buy or not
    if random.choice([1, 0]):
        buyAircraft = random.choice([boeing1, boeing2, boeing3, boeing4, boeing5, boeing6, airbus1, airbus2, airbus3,
                                     airbus4, airbus5, airbus6])
        toubal.buy_aircraft(buyAircraft)
        # choice if company oualladi want to buy or not
    if random.choice([1, 0]):
        buyAircraft2 = random.choice([boeing1, boeing2, boeing3, boeing4, boeing5, boeing6, airbus1, airbus2, airbus3,
                                     airbus4, airbus5, airbus6])
        oualladi.buy_aircraft(buyAircraft2)
        # choice if company toubal want to sell or not
    if random.choice([1, 0]):
        buyAircraft = random.choice([boeing1, boeing2, boeing3, airbus1, airbus2, airbus3])
        toubal.sell_aircraft(buyAircraft)
        # choice if company oualladi want to sell or not
    if random.choice([1, 0]):
        buyAircraft2 = random.choice([boeing1, boeing2, boeing3, airbus1, airbus2, airbus3])
        oualladi.sell_aircraft(buyAircraft2)
    # Simuler le processus de développement pour les avions en cours de développement
        # choice if company toubal want to develop or not
    if random.choice([1, 0]):
        boeing = aircraft.Aircraft("Boeing", 0, 0, 0, 0, 0, False)
        toubal.develop_aircraft(boeing)
        # choice if company oualladi want to develop or not
    if random.choice([1, 0]):
        airbus = aircraft.Aircraft("Airbus", 0, 0, 0, 0, 0, True)
        oualladi.develop_aircraft(airbus)
    # Demander aux joueurs de prendre des décisions stratégiques pour leur entreprise
        # choice if they take decision
    if random.choice([1, 0]):
        # choice if decision is cooperation
        if random.choice([1, 0]):
           print("-The company take decision of cooperation")
           cash_cooperation = toubal.cash + oualladi.cash
           cooperation = cooperation.Cooperation(cash_cooperation)
           print(f"cash of players before cooperation toubal is {toubal.cash} and oualladi {oualladi.cash}")
           # choice type of plane airbus
           if random.choice([1, 0]):
               airbus = aircraft.Aircraft("Airbus", 0, 0, 0, 0, 0, True)
               cooperation.develop_aircraft(airbus,toubal,oualladi)
           else:
               boeing = aircraft.Aircraft("Boeing", 0, 0, 0, 0, 0, False)
               cooperation.develop_aircraft(boeing, toubal, oualladi)
           print(f"cash of players after cooperation toubal is {toubal.cash} and oualladi {oualladi.cash}")

    # Vérifier si l'un des joueurs a perdu tous ses avions ou fait faillite
    # Si le jeu est terminé, afficher le vainqueur et terminer la boucle de jeu
