"""
Stars order of events
19. Population grows/dies
"""

# TODO: use hab values
# TODO: add in crowding
# TODO: deal with overcrowding

from .tools import get_owner

def run(universe, orders=None):
    for planet in universe['planets']:
        if 'population' in planet:
            player = get_owner(universe, planet)
            pgr = (100 + player['pop_growth']) / 100.
            planet['population'] = int(planet['population']) * pgr
    return universe
