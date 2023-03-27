import aircraft
import player
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
    boeing = aircraft.Aircraft("Boeing", 0, 0, 0, 0, 0)
    airbus = aircraft.Aircraft("Airbus", 0, 0, 0, 0, 0)
        # choice if company toubal want to develop or not
    if random.choice([1, 0]):
        toubal.develop_aircraft(boeing)
        # choice if company oualladi want to develop or not
    if random.choice([1, 0]):
        oualladi.develop_aircraft(airbus)
    # Demander aux joueurs de prendre des décisions stratégiques pour leur entreprise
    # Vérifier si l'un des joueurs a perdu tous ses avions ou fait faillite
    # Si le jeu est terminé, afficher le vainqueur et terminer la boucle de jeu
