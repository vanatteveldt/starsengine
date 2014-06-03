"""
Stars order of events
19. Population grows/dies
"""

from .tools import get_owner, get_hab

def run(universe, orders=None):
    for planet in universe['planets']:
        if 'population' in planet:
            player = get_owner(universe, planet)
            planet['population'] = growth(planet, player)
    return universe

def new_population(planet, player)
    pgr = player['pop_growth']
    hab = get_hab(planet, player)/100
    if player['prt']="HE":
        pgr=pgr*2
    elif player['prt']="AR":
        max_pop=planet['orbital']
        if planet['orbital']="Fort":
            max_pop=250000
        elif planet['orbital']="Dock":
            max_pop=500000
        elif planet['orbital']="Station":
            max_pop=1000000
        elif planet['orbital']="Ultra":
            max_pop=2000000
        elif planet['orbital']="DeathStar":
            max_pop=3000000
    elif player['prt']="JoAT":
        max_pop=1200000*hab
    else:
        max_pop=1000000*hab
    
    if player['obrm']:
        max_pop=max_pop*1.1

    growth=(100+pgr)/100 * hab

    if hab < 0: #RED planets kill at 10% of their -ve value
        return int(planet['population'] * (1-(hab/10))
    elif planet['population'] <= (.25 * max_pop): # Uncrowded planet growth is unrestricted
        return int(planet['population'] * growth)    
    elif planet['population'] <= max_pop: # Crowding reduces growth
        crowding=16/9*(1-planet['population']/max_pop)^2
        return int(planet['population'] * growth * crowding)
    elif planet['population'] >= 4*max_pop: # Massive overpop dies at 12%
        return int(planet['population'] * (1-.12))
    else: # Overpop death is linear up to 12%
        over_pop=(planet['population']-max_pop)/(3*max_pop)
        return int(planet['population'] * (1-((1-over_pop)*.12)) )
        
