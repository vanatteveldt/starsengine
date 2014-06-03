from nose.tools import assert_equal, assert_not_equal, assert_true

from engine.tools import get_hab

def test_hab():
    planet = {"hab": [20, 20, 20]}
    player = {"hab": ["immune", "immune", "immune"]}
    assert_equal(get_hab(planet, player), 100)

    player = {"hab": ["immune", "immune", [10,30,20]]}
    assert_equal(get_hab(planet, player), 100)

    player = {"hab": [[10,30,20], [10,30,20], [10,30,20]]}
    assert_equal(get_hab(planet, player), 100)

    player = {"hab": ["immune", "immune", [30,50,40]]}
    assert_true(get_hab(planet, player) < 0)
