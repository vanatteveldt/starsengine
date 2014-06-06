"""
Stars! turn processing
"""

from . import move_fleets, pop_growth, mining

def process_turn(universe, orders):
    """
    Process a turn, creating new turn and orders
    @param universe: a (json) dictionary containing the state of the universe
    @param orders: a set of json dictionaries containing player orders
    @return: the new state of the universe
    """

    # Turn elements (based on http://www.starsfaq.com/order_events.htm)
    # 1 Scrapping fleets (with possible tech gain)
    # 2 * Waypoint 0 load tasks (if done by hand) *
    # 3 Waypoint 0 unload tasks
    # 4 Waypoint 0 Colonization/Ground Combat resolution (with possible tech gain)
    # 5 Waypoint 0 load tasks (if done via task tile order)
    # 6 * Other Waypoint 0 tasks *
    # 7 MT moves
    # 8 In-space packets move and decay
    #   a PP packets (de)terraform
    #   b Packets cause damage
    #   c * Planets that where hit and end up with 0 colonists become uninhabited*
    # 9 Wormhole entry points jiggle

    # 10 Fleets move
    universe = move_fleets.run(universe, orders)

    # 11 Inner Strength colonists grow in fleets
    # 12 Mass Packets still in space and Salvage decay
    # 13 Wormhole exit points jiggle
    # 14 Wormhole endpoints degrade/jump
    # 15. SD Minefields detonate (possibly damaging again fleet that hit minefield during movement)
    # 16. Mining
    universe = mining.run(universe, orders)

    # 17. Production (incl. research, packet launch, fleet/starbase construction)
    # 18. SS Spy bonus obtained
    # 19. Population grows/dies
    universe = pop_growth.run(universe, orders)

    # 20. Packets that just launched and reach their destination cause damage
    # 21. Random events (comet strikes, etc.)
    # 22. Fleet battles (with possible tech gain)
    # 23. Meet MT
    # 24. Bombing
    #   * Player 1 bombing calculated *
    #   * Normal/LBU Bomb Damage Calculated *
    #   * Smart Bomb Damage Calculated *
    #   * Defences Recalculated *
    #   * Player 2 bombing calculated and so on in order with players 3, 4... *
    # 25 Planets with 0 colonists become uninhabited (lose starbase and defences) *
    # 26 Waypoint 1 unload tasks
    # 27 Waypoint 1 Colonization/Ground Combat resolution (with possible tech gain)
    # 28 Waypoint 1 load tasks
    # 29 Mine Laying
    # 30 Fleet Transfer
    # 31 * Waypoint 1 Fleet Merge *
    # 32 CA Instaforming
    # 33 * Minefield Decay *
    # 34 Mine sweeping
    # 35 Starbase and fleet repair
    # 36 Remote Terraforming

    return universe
