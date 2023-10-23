# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:46:43 2023

@author: 1
"""
from p2p import Peer2PeerNode
from merkle_tree import get_merkle_tree, decompress_zip
import os
import json
import time

node2 = Peer2PeerNode("localhost", 9001)
node2.start()
time.sleep(1)
node2.connect_with_node('localhost', 9000)
time.sleep(5)

# File path here.
zip_file_path = 'D:\\data.zip'
# Decompress zip file...
decompress_zip(zip_file_path)

# Get same folder name as zip file by default.
merkle_tree = get_merkle_tree(os.path.splitext(zip_file_path)[0])

# Write merkle_tree to json file.
with open('tree.json', 'w') as f:
    # Use json.dump to write the dictionary to the file
    json.dump(merkle_tree, f)

node2.send_tree_data("tree.json")

"""
This is test message.

node2.send_to_nodes({"message" : "Hellow"})
"""