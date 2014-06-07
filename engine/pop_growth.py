"""
Stars order of events
19. Population grows/dies
"""

#TODO: AR

from .tools import get_owner, get_hab

def run(universe, orders=None):
    for planet in universe['planets']:
        if 'population' in planet:
            player = get_owner(universe, planet)
            planet['population'] = new_population(planet, player)

def new_population(planet, player):
    hab = get_hab(planet, player)

    # hab is a percentage (-45-100), so multiply by 10k rather than 1M
    if player['prt'] == "JOAT":
        max_pop = 12000 * hab
    else:
        max_pop = 10000 * hab
    if 'OBRM' in player['lrt']:
        max_pop *= 1.1

    def round(x):
        # round pop down to 100 colonist units
        return int(x/100) * 100

    population = planet['population']
    # calculate effective growth rate as percentage
    if hab < 0: #RED planets kill at 10% of their -ve value
        return round(population * (1 + hab/1000))
    elif population >= 4*max_pop: # Massive overpop dies at 12%
        return round(population * .88)
    elif population > max_pop: # Overpop death is linear up to 12%
        over_pop=(population-max_pop)/(3*max_pop)
        return round(population * (1-(over_pop*.12)))
    else:
        # planet can grow
        growth = population * (player['pop_growth']/100) * (hab/100)
        if population > (.25 * max_pop): # Crowding reduces growth
            crowding=16/9*(1-population/max_pop)**2
            growth *= crowding
        return population + round(growth)
