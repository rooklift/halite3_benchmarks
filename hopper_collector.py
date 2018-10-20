#!/usr/bin/env python3
F=False
U=True
V=range
G=max
c=None
X=len
import itertools
l=itertools.chain
import hlt
from hlt import constants
from hlt.positionals import Direction
import random
import logging
Y=logging.info
Q=hlt.Game()
Q.ready("HopperCollector")
Y("Successfully created bot! My Player ID is {}.".format(Q.my_id))
Y("{}".format(constants.SHIP_COST))
plans={}
def t(u,me,e):
	if me.halite_amount+e.halite_amount+u[e.position].halite_amount<4000:
		return F
	for W in l([me.shipyard],me.get_dropoffs()):
		if u.calculate_distance(W.position,e.position)<5:
			return F
	return U
while U:
	Q.update_frame()
	me=Q.me
	u=Q.game_map
	q=F
	g=[]
	for M in V(0,u.height,8):
		for C in V(0,u.width,8):
			B=0
			K=(C,M)
			o=0
			for y in V(M,M+8):
				for x in V(C,C+8):
					L=u[hlt.Position(x,y)].halite_amount
					B+=L
					if L>o:
						K=(x,y)
						o=L
			if B>3000:
				g.append((K[0],K[1],B/(1+u.calculate_distance(hlt.Position(C+4,M+4),me.shipyard.position))))
	T=G(g,key=lambda x:x[2])
	h=[]
	p=[me.shipyard.position]+[W.position for W in me.get_dropoffs()]
	for e in me.get_ships():
		if e.position in p:
			plans[e.id]=c
		if plans.get(e.id)=='return' or e.halite_amount>700:
			plans[e.id]='return'
			w=me.shipyard.position
			s=9999
			for H in p:
				d=u.calculate_distance(e.position,H)
				if d<s:
					s=d
					w=H
			d=u.naive_navigate(e,w)
			h.append(e.move(d))
		elif not q and t(u,me,e):
			q=U
			h.append(e.make_dropoff())
		elif u[e.position].halite_amount<constants.MAX_HALITE/10:
			w=hlt.Position(T[0],T[1])
			d=u.naive_navigate(e,w)
			h.append(e.move(d))
		else:
			h.append(e.stay_still())
	if X(me.get_ships())<15 and Q.turn_number<=200 and me.halite_amount>=constants.SHIP_COST and not u[me.shipyard].is_occupied:
		h.append(Q.me.shipyard.spawn())
	Q.end_turn(h)
