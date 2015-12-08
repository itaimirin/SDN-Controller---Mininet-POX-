"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        leftHost2 = self.addHost( 'h2' )
        leftHost3 = self.addHost( 'h3' )
        leftSwitch = self.addSwitch( 's3' )
        
        # Add links to LEFT SWITCH
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftHost2, leftSwitch )
        self.addLink( leftHost3, leftSwitch )   
topos = { 'mytopo': ( lambda: MyTopo() ) }
