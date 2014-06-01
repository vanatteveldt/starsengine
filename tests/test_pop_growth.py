from nose.tools import assert_equal, assert_not_equal

from engine import pop_growth
from engine.tools import get_planet

def test_growth():
    universe = {"planets": [{"id": 1, "owner": 1, "population": 1000}],
                "players": [{"id": 1, "pop_growth": 10}]}

    result = pop_growth.run(universe)
    assert_equal(get_planet(result, 1)['population'], 1100)
