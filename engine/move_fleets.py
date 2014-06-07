"""
Stars order of events
10. Fleets move
"""

from .tools import get_fleet, calc_distance

#TODO: too much to mention

def run(universe, orders):
    for order in orders:
        for fleetorder in order.get('fleetorders', []):
            move_fleet(universe, fleetorder)

def move_fleet(universe, fleetorder):
    fleet = get_fleet(universe, fleetorder['fleet'])

    speed = fleetorder['warp'] ** 2
    dist = calc_distance(fleet, fleetorder)

    if int(dist) <= speed:
        fleet['x'], fleet['y'] = fleetorder['x'], fleetorder['y']
    else:
        frac = speed / dist
        for coord in ('x', 'y'):
            fleet[coord] += int(frac * (fleetorder[coord] - fleet[coord]))
