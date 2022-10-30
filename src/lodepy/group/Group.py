from typing import List, Set
from lodepy.nodes.Node import Node

class Group():
    def __init__(self, name: str, nodes: Set[Node]):
        self.name: str = name
        self.nodes: Set[Node] = nodes

    def add_node(self, node):
        self.nodes.add(node)