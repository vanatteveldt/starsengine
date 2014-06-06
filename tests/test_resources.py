from nose.tools import assert_equal, assert_not_equal, assert_greater

from engine.tools import get_resources, get_max_factories

def test_max_factories():
    player = {"factories": {"max": 9}}
    planet = {"population": 25000}
    assert_equal(get_max_factories(planet, player), 22)
    planet = {"population": 33000}
    assert_equal(get_max_factories(planet, player), 29)


def test_resources():
    player = {"pop_efficiency": 1000,
              "factories": {"max": 15, "efficiency": 9}
              }

    def _get_resources(pop, fact):
        planet = {"population": pop, "installations": {"factories": fact}}
        return get_resources(planet, player)

    assert_equal(_get_resources(43700, 12), 54)
    assert_equal(_get_resources(57700, 17), 73)
    assert_equal(_get_resources(66400, 17), 82)
