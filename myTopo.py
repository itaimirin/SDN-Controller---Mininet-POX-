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
        rightHost = self.addHost( 'h3' )
        rightHost2 = self.addHost( 'h4' )
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )

        # Add links to LEFT SWITCH
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftHost2, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )
        self.addLink( rightSwitch, rightHost2 )
topos = { 'mytopo': ( lambda: MyTopo() ) }
