# SDN-Controller---Mininet-POX-
The objective of this small project was to learn to program an SDN controller using the POX platform

-----------------------------------
README - Programming a SDN Controller for mininet using the POX platform 
-----------------------------------
contains:

IM_l2_learning.py
mytopo.py
mytopo2.py


IM_l2_learning.py  - is my controllers Layer 2 Learning script

mytopo.py - is one of my topologies (2 hosts and 2 switches )
mytopo2.py - is on of my topologies (3 hosts and 1 switch )

HOW TO RUN:
1. Run the Controller using pox.py: 
	./pox.py forwading.IM_l2_learning
	
2. Intantiated the topology with the controller using: 
	Sudo mn --controller=remote,ip=127.0.0.1, port=6633 --custom mytopo(2).py --topo mytopo 

