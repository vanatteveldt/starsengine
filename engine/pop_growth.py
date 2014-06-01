"""
Stars order of events
19. Population grows/dies
"""

# TODO: use hab values
# TODO: add in crowding
# TODO: deal with overcrowding

def run(universe, orders):
    for planet in universe['planets']:
        if 'population' in planet:
            assert 'owner' in planet
            race = get_race(planet['owner'])
            pgr = (100 + race['pop_growth']) / 100.
            planet['population'] = int(planet['population']) * pgr
    return universe
