"""
Stars order of events
16. Mining
"""

# TODO:
# - Mineral depletion (see http://starsautohost.org/sahforum2/index.php?t=msg&th=5405&prevloaded=1&rid=1803&start=150#msg_num_6)
# - AR

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
            mined = int(conc * mines * player['mines']['efficiency'] / 1000)
            planet['mineral_surface'][mineral] += mined
