#!/usr/bin/env python3
f=True
A=range
a=max
w=None
e=len
import hlt
from hlt import constants
from hlt.positionals import Direction
import random
import logging
p=logging.info
v=hlt.Game()
v.ready("PriorityCollector")
p("Successfully created bot! My Player ID is {}.".format(v.my_id))
p("{}".format(constants.SHIP_COST))
b={}
while f:
	v.update_frame()
	me=v.me
	u=v.game_map
	F=[]
	for j in A(0,u.height,8):
		for R in A(0,u.width,8):
			M=0
			i=(R,j)
			W=0
			for y in A(j,j+8):
				for x in A(R,R+8):
					L=u[hlt.Position(x,y)].halite_amount
					M+=L
					if L>W:
						i=(x,y)
						W=L
			if M>3000:
				F.append((i[0],i[1],M/(1+u.calculate_distance(hlt.Position(R+4,j+4),me.shipyard.position))))
	O=a(F,key=lambda x:x[2])
	G=[]
	for m in me.get_ships():
		if m.position==me.shipyard.position:
			b[m.id]=w
		if b.get(m.id)=='return' or m.halite_amount>700:
			b[m.id]='return'
			x=me.shipyard.position
			V=u.naive_navigate(m,x)
			G.append(m.move(V))
		elif u[m.position].halite_amount<constants.MAX_HALITE/10:
			x=hlt.Position(O[0],O[1])
			V=u.naive_navigate(m,x)
			G.append(m.move(V))
		else:
			G.append(m.stay_still())
	if e(me.get_ships())<15 and v.turn_number<=200 and me.halite_amount>=constants.SHIP_COST and not u[me.shipyard].is_occupied:
		G.append(v.me.shipyard.spawn())
	v.end_turn(G)
