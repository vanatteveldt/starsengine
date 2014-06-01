Stars! data structures
====

A number of common datastructures are needed to get modules to talk together.
The current proposal is to have all data in (json) dictionaries, e.g. consist of (nested) dictionaries, lists and primitives like integers, and strings.
These are in no way final data structures, they will be added to and modified as needed during development.

The current data structure is given below, with nesting indicating nested dictionaries and labels being keys. 



Universe
====

The universe represents the state of the universe at a single turn. 
No effort is made to separate 'permanent' (star location) from 'variable' information, since almost all information is variable. 

+ players (list)
  + id
  + prt (string)
  + lrt (list of strings)
  + pop_growth (integer range 1-20)
  + tech_levels (list or dict of int range 0-26)
  + tech_invested (list or dict of int with # of points invested)
+ planets (list)
  + name (string)
  + x
  + y
  + mineral_concentration (list of iro, bor, ger, int range 0-100+)
  + mineral_surface (list of iro, bor, ger, int in ktons)
  + installations
    + factories
    + mines
    + defenses
  + owner (id)
  + population (int in ktons)
+ fleets (list)
  + owner (id)
  + id
  + name (string)
  + x
  + y
  
Orders
====

An order is a file containing one player's turn orders.

+ player (id)
+ fleetorders (list)
  + fleet (id)
  + x
  + y
  + warp


Example json file 
====

To show how the bulleted lists are to be interpreted, below is an example json file for orders:

```json
{"player": 1,
 "fleetorders": [
   {"fleet": 1, "x": 120, "y": 120}
 ]
}
```
