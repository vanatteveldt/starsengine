"""
Stars order of events
16. Mining
"""

from .tools import get_owner

def run(universe, orders=None):
    for planet in universe['planets']:
        if 'owner' in planet:
            player = get_owner(universe, planet)
            mine(planet, player)


def mine(planet, player):
    mines = planet['installations'].get('mines')
    if mines:
        for mineral, conc in planet['mineral_concentration'].items():
            mined = int(conc * mines * player['mining']['efficiency'] / 1000)
            planet['mineral_surface'][mineral] += mined
