from typing import List
from lodepy.nodes.Node import Node


class Group():
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes