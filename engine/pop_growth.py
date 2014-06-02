"""
Stars order of events
19. Population grows/dies
"""

# TODO: deal with overcrowding (confirm formula, I made one up!)
# TODO: deal with red planets

from .tools import get_owner, get_hab

def run(universe, orders=None):
    for planet in universe['planets']:
        if 'population' in planet:
            player = get_owner(universe, planet)
            planet['population'] = growth(planet, player)
    return universe

def new_population(planet, player)
    pgr = player['pop_growth']
    hab = get_hab(planet, player)
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

    growth=(100+pgr)/100

    if planet['population'] <= (.25 * max_pop):
        return int(planet['population'] * growth)    
    if planet['population'] <= max_pop:
        crowding=16/9*(1-planet['population']/max_pop)^2
        return int(planet['population'] * growth * crowding)
    if planet['population'] > max_pop:
        over_pop=(planet['population']-*max_pop)
        death=over_pop*over_pop/max_pop #Excess pop dies at the rate at which is it overpopped. FIXME
        return int(planet['population']-death)
        
