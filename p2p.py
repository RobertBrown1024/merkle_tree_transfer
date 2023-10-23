# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 08:15:19 2023

@author: 1
"""
from p2pnetwork.node import Node
from tqdm import tqdm
import os

BUFFER_SIZE = 1024 * 2
class Peer2PeerNode(Node):
    def __init__(self, host, port):
        super(Peer2PeerNode, self).__init__(host, port, None)
        self.merkle_tree = {}
        self.bytes = b''
        self.sendflag = True
        print("MyNode: Started")

    def outbound_node_connected(self, node):
        print("outbound_node_connected: " + node.id)

    def inbound_node_connected(self, node):
        print("inbound_node_connected: " + node.id)

    def inbound_node_disconnected(self, node):
        print("inbound_node_disconnected: " + node.id)

    def outbound_node_disconnected(self, node):
        print("outbound_node_disconnected: " + node.id)

    def node_disconnect_with_outbound_node(self, node):
        print("node wants to disconnect with oher outbound node: " + node.id)

    def node_request_to_stop(self):
        print("node is requested to stop!")

    def node_message(self, connected_node, data):
        
        if str(data) == "sendflag":
            self.sendflag = True
        elif type(data) == dict:
            if "tree_data_end" in data.keys():
                self.save_file()
        else: 
            print("first here")
            self.bytes += data.encode()
            self.send_to_nodes("sendflag")


        
    def set_merkle_tree(self, tree):
        self.merkle_tree = tree
        print(self.merkle_tree)
    
    def send_tree_data(self, filename):
        filesize = os.path.getsize(filename)
        progress = tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, 'rb') as file:
            while True:
                if self.sendflag:
                    chunk = file.read(BUFFER_SIZE)  # Read 1024 bytes at a time
                    if not chunk:
                        break
                    self.sendflag = False
                    self.send_to_nodes(chunk)
                    progress.update(len(chunk))
        self.send_to_nodes({"tree_data_end" : ""})
                
    def save_file(self):
        with open("write.json", 'wb') as file:
            file.write(self.bytes) 
