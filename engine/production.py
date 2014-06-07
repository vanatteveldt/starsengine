"""
Stars order of events
17. Production
"""

# TODO:
# - fractional production
# - defenses, terraforming
# - fleets

from .tools import get_planet, get_owner, get_resources

def run(universe, orders=None):
    for order in orders:
        for production_order in order.get('production', []):
            produce(universe, production_order)

def unit_cost(player, order_item):
    """
    Return the cost of producing a single unit of order_item
    @returns a dict {"resources": X, "germanium": X} with keys as needed
    """
    if order_item['object'] == 'factories':
        return {"resources": player['factories']['cost'],
                "germanium": player['factories']['cost_germanium']
                }
    elif order_item['object'] == 'mines':
        return {"resources": player['mines']['cost']}
    else:
        raise ValueError("Unknown production item")

def max_quantity(resources, planet, cost):
    """
    Return the max quantity (incl. fraction) of an item that can be produced
    """
    result = None
    available = dict(resources=resources, **planet['mineral_surface'])
    for var, c in cost.items():
        can_produce = available.get(var, 0) / c
        result = can_produce if result is None else min(result, can_produce)
    return result

def produce(universe, order):
    planet = get_planet(universe, order['planet'])
    player = get_owner(universe, planet)
    # TODO check owner == order player
    resources = get_resources(planet, player)
    # TODO research percentage
    for item in order['queue']:
        # How many can we produce?
        # TODO partial production, we just drop the fraction for now
        cost = unit_cost(player, item)
        maxq = int(max_quantity(resources, planet, cost))
        q = min(maxq, item['quantity'])
        # pay the cost
        for var, c in cost.items():
            if var == "resources":
                resources -= c * q
            else:
                planet['mineral_surface'][var] -= c*q
        # add the installations
        planet['installations'][item['object']] += q
        if q < item['quantity']:
            return resources  # goes to science (=TODO)
