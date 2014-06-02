Stars! Engine
===========

Engine for an open source stars! clone

This is an attempt at an open source stars! clone.
I realize that there have been a number of attempts in the past, so hopefully this can succeed by openness and modularity.

*Development Status*: Extremely early [![Build Status](https://travis-ci.org/vanatteveldt/starsengine.png)](https://travis-ci.org/vanatteveldt/starsengine) 

This repository will only hold the engine code, i.e. the code that transforms a turn plus orders into the next turn. 
The webserver and client(s) will get their own repository.

Design
====

1. The "engine" is responsible to turning universe+orders into a new universe. 
2. Some other program (e.g. the current starserver stub) is responsible to handling the external interface, validating and merging files, keeping track of state, etc etc. 
3. The engine consists of approximately* one module for each item in the order of events
4. Each module takes universe+orders as input and outputs the new universe (optionally plus the orders)


python-pseudocode for the engine (taking http://www.starsfaq.com/order_events.htm as reference)

```python
def process_turn(universe, orders):
   universe = scrapping_fleets(universe, orders)
   universe = manual_load(universe, orders)
   universe = wp0_unload(universe, orders)
   ....
   universe = remote_terraform(universe, orders) 
   return universe
```
