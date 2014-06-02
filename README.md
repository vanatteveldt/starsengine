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

Testing
====

Unit testing is important for any good program, but especially for 'backend' code test-driven development is a great way to write good code.
The basic idea of test driven development is that you write unit tests before writing the actual code, 
and add specific tests for any corner case you can think of.
During development, you don't run the normal code or separate __main__ code to test, but use the unit tests for this.

We currently use nose tests, which can be used simply by typing `nosetests` from the console in the repository folder (or in your favourite IDE). You can also specify a specific test to run, e.g. `nosetests tests/test_pop_growth.py`. 

Every push is also automatically unit tested by travis, and a developer that 'breaks' a build will get an automatic email about it. 






