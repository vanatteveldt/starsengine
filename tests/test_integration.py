from nose.tools import assert_equal

from engine.engine import process_turn

def test_integration():
    """
    General integration test.

    The idea is to have a universe/orders representation that captures
    as many different aspects as possible. Where non-trivial interaction
    between modules is possible, it should also be tested here.

    When writing/updating new engine modules, please also update this test!
    """


    planet = {"id": 1, "owner": 1, "hab": [50, 50, 50]}

    universe = {
        "planets": [{"id": 1, "owner": 1,
                     "hab": [50, 50, 50],
                     "mineral_concentration": {"boranium": 100, "ironium": 69, "germanium": 35},
                     "mineral_surface": {"boranium": 50, "ironium": 20, "germanium": 18},
                     "installations": {"mines": 10, "factories": 1},
                     "population": 25000
                     }],
        "players": [{"id": 1, "pop_efficiency": 1000,
                     "mines": {"max": 10, "efficiency": 10},
                     "factories": {"max": 10, "efficiency": 10, "cost": 10, "cost_germanium": 4},
                     "pop_growth": 15,
                     "prt": "WM", "lrt": [],
                     "hab": ["immune", "immune", "immune"]
                 }],
        "fleets": [{"id": 1, "x": 0, "y": 0}]
    }

    orders = [{"player": 1,
               "production": [
                   {"planet": 1, "queue": [{"object": "factories", "quantity": 2}]}
               ],
               "fleetorders": [
                   {"fleet": 1, "x": 100, "y": 0, "warp": 5}
               ]}]

    process_turn(universe, orders)

    # remove caches
    universe = {k:v for k,v in universe.items() if not k.startswith("__")}

    new_germ = 18 + 3 - 8
    expected = {
        "planets": [{"id": 1, "owner": 1,
                     "hab": [50, 50, 50],
                     "mineral_concentration": {"boranium": 100, "ironium": 69, "germanium": 35},
                     "mineral_surface": {"boranium": 60, "ironium": 26, "germanium": new_germ},
                     "installations": {"mines": 10, "factories": 3},
                     "population": 28700
                     }],
        "players": [{"id": 1, "pop_efficiency": 1000,
                     "mines": {"max": 10, "efficiency": 10},
                     "factories": {"max": 10, "efficiency": 10, "cost": 10, "cost_germanium": 4},
                     "pop_growth": 15,
                     "prt": "WM", "lrt": [],
                     "hab": ["immune", "immune", "immune"]
                 }],
        "fleets": [{"id": 1, "x": 25, "y": 0}]
    }

    # check result per key for more readable output
    for key in set(universe) | set(expected):
        assert_equal(universe.get(key), expected.get(key))
