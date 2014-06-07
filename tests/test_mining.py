from nose.tools import assert_equal, assert_not_equal, assert_greater

from engine import mining

def test_growth():
    planet = {"id": 1, "owner": 1,
              "mineral_concentration": {"boranium": 100, "ironium": 69, "germanium": 35},
              "mineral_surface": {"boranium": 50, "ironium": 20, "germanium": 18},
              "installations": {"mines": 10}
              }
    player = {"id": 1,
              "mines": {"max": 10, "efficiency": 10}
              }

    result = mining.run({"planets": [planet], "players": [player]}, None)

    assert_equal(planet['mineral_surface'], {"boranium": 60, "ironium": 26, "germanium": 21})
