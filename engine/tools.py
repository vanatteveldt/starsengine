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

def get_hab(planet, player):
    """
    Compute the hab value for a planet for a given player
    """
    planet_value_points=0
    ideality=10000
    red_value=0
    
    for i in range(0,3):
        distance=abs(player['hab'][i][3] - planet['hab'][i])
        if planet['hab'][i] > player['hab'][i][3]:
            radius=player['hab'][i][2] - player['hab'][i][3]
        else:
            radius=player['hab'][i][3] - player['hab'][i][1]
        if player['hab'][i] = "immune":
            planet_value_points += 10000
        elif planet['hab'][[i] < player['hab'][i][2] and planet['hab'][i] > player['hab'][i][1]:
            excent=100-(int(100*distance/radius)
            planet_value_point =+ excent^2
            if distance *2 > radius: #Outer quarter of hab range gets a penalty
                ideality=ideality*(3/2 - (distance/radius))
        else: #Red on this variable
            red_value+=max(-15,radius-distance)

    if red_value != 0:
        return red_value
    planet_value_points = sqrt(planet_value_points/3)+0.9
    planet_value_points = planet_value_points * int(ideality)/10000
    return int(planet_value_points)
