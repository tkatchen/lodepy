from typing import List, Set
from lodepy.nodes.Node import Node


class Group():
    def __init__(self, nodes: Set[Node]):
        self.nodes = nodes

    def add_node(self, node):
        self.nodes.add(node)