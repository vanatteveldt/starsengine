"""
Generic code shared between different engine modules
"""

import math

def get_object(json, key, id):
    """
    Get an object from json[key] so that json[key]['id'] == id
    Construct a temporary index in json[__key_index]
    Will raise a KeyError if the id is not found
    """
    index_name = "__"+key
    if index_name not in json:
        json[index_name] = {o['id'] : o for o in json[key]}
    return json[index_name][id]

def get_fleet(universe, fleet_id):
    """
    Get a fleet by id.
    """
    return get_object(universe, "fleets", fleet_id)


def get_planet(universe, planet_id):
    """
    Get a planet by id.
    """
    return get_object(universe, "planets", planet_id)

def get_owner(universe, obj):
    """
    Get the owner of the given object, which should have a 'owner' attribute
    """
    return get_object(universe, "players", obj['owner'])

def calc_distance(a, b):
    """
    Compute the distance between a and b
    Both objects should have ['x'] and ['y'] keys
    """
    return math.sqrt((a['x'] - b['x'])**2 + (a['y'] - b['y'])**2)
