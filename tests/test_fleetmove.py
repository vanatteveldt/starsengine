from nose.tools import assert_equal, assert_not_equal

from engine import move_fleets
from engine.tools import get_fleet

def test_travel():
    universe = {"fleets": [{"id": 1, "x": 0, "y": 0}]}

    def assert_location(fleet_id, x, y):
        f = get_fleet(universe, fleet_id)
        assert_equal(f['x'], x)
        assert_equal(f['y'], y)

    # move from to 100,0 at warp 5
    order = {"fleetorders": [
        {"fleet": 1, "x": 100, "y": 0, "warp": 5}
    ]}

    move_fleets.run(universe, [order])
    assert_location(1, 25, 0)

    # Don't overshoot
    order = {"fleetorders": [
        {"fleet": 1, "x": 25, "y": 25, "warp": 9}
    ]}
    move_fleets.run(universe, [order])
    assert_location(1, 25, 25)

    # moving 25.7 ly at warp 5 gets there in one turn
    order = {"fleetorders": [
        {"fleet": 1, "x": 25, "y": 5, "warp": 5}
    ]}
    move_fleets.run(universe, [order])
    assert_location(1, 25, 5)
