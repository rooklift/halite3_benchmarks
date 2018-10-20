#!/usr/bin/env python3
e=True
import hlt
from hlt import constants
from hlt.positionals import Direction
x=Direction.West
g=Direction.East
P=Direction.South
u=Direction.North
import random
z=random.choice
import logging
Q=logging.info
o=hlt.Game()
o.ready("Collector")
Q("Successfully created bot! My Player ID is {}.".format(o.my_id))
while e:
	o.update_frame()
	me=o.me
	X=o.game_map
	A=[]
	for a in me.get_ships():
		if a.halite_amount>500:
			Y=me.shipyard.position
			s=X.naive_navigate(a,Y)
			A.append(a.move(s))
		elif X[a.position].halite_amount<constants.MAX_HALITE/10:
			L=z([u,P,g,x])
			Y=a.position.directional_offset(L)
			s=X.naive_navigate(a,Y)
			A.append(a.move(s))
		else:
			A.append(a.stay_still())
	if o.turn_number<=200 and me.halite_amount>=constants.SHIP_COST and not X[me.shipyard].is_occupied:
		A.append(o.me.shipyard.spawn())
	o.end_turn(A)
