from nose.tools import assert_equal, assert_not_equal, assert_greater

from engine import pop_growth
from engine.tools import get_hab

def test_growth():
    planet = {"id": 1, "owner": 1, "hab": [50, 50, 50]}
    player = {"id": 1, "pop_growth": 15,
              "prt": "WM", "lrt": [],
              "hab": ["immune", "immune", "immune"]}
    universe = {"planets": [planet],
                "players": [player]}

    def growth(pop):
        planet['population'] = pop
        result = pop_growth.run(universe)
        return planet['population'] - pop

    assert_equal(growth(10000), 1500)
    assert_equal(growth(11500), 1700)

    # 25% is still max, 33% optimal, 100% no growth
    # http://wiki.starsautohost.org/wiki/%22Table_of_Population_Growth%22_by_James_Rasbeck_1997_v2.6/7
    assert_equal(growth(250000), 37500)
    assert_equal(growth(333300), 39500)
    assert_equal(growth(1000000), 0)
    assert_greater(growth(333300), growth(320000))
    assert_greater(growth(333300), growth(340000))

    # massive overpop
    assert_equal(growth(10000000), -1200000)
    # CHECKME: which side does rounding go? aka floor or int?
    assert_equal(growth(10000100), -1200100)

    assert_equal(growth(2000000), -80000)
    assert_equal(growth(3000000), -240000)
    assert_equal(growth(4000000), -480000)

    # Red planet
    player["hab"][2] = [60, 80, 70]
    assert_equal(get_hab(planet, player), -10)
    assert_equal(growth(100000), -1000)
