from typing import Set
from lodepy.nodes.node import Node

class Group():
    '''
    A group, which is a collection of nodes
    '''
    def __init__(self, name: str, nodes: Set[Node]):
        self.name: str = name
        self.nodes: Set[Node] = nodes

    def add_node(self, node: Node) -> None:
        '''
        Add a node to this group
        '''
        self.nodes.add(node)
