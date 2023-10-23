# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:47:56 2023

@author: 1
"""
from p2p import Peer2PeerNode
import time

node = Peer2PeerNode("localhost", 9000)
node.start()
time.sleep(1)

