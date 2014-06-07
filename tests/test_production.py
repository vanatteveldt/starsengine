from nose.tools import assert_equal, assert_not_equal, assert_greater

from engine import production

def test_production():
    planet = {"id": 1, "owner": 1,
              "mineral_surface": {"boranium": 50, "ironium": 20, "germanium": 22},
              "installations": {"factories": 1},
              "population": 25000
              }
    player = {"id": 1, "pop_efficiency": 1000,
              "factories": {"max": 10, "efficiency": 10, "cost": 10, "cost_germanium": 4}
              }
    universe = {"planets": [planet], "players": [player]}


    order = {"production": [
        {"planet": 1, "queue": [{"object": "factories", "quantity": 2}]}
    ]}

    # build two factories
    production.run(universe, [order])
    assert_equal(planet['installations']['factories'], 3)
    assert_equal(planet['mineral_surface']['germanium'], 14)

    # two more factories
    production.run(universe, [order])
    assert_equal(planet['installations']['factories'], 5)
    assert_equal(planet['mineral_surface']['germanium'], 6)

    # try two more factories, run out of germanium, only build one
    production.run(universe, [order])
    assert_equal(planet['installations']['factories'], 6)
    assert_equal(planet['mineral_surface']['germanium'], 2)
