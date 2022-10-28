from typing import TypeVar

from lodepy.nodes.Node import Node

K = TypeVar('K')

class NodeReturn(Node):
    def __init__(self, node: Node, value: K):
        super(node)
        self.value = value

    def __str__(self) -> K:
        return self.value

    def __eq__(self, other: 'NodeReturn') -> bool:
        if isinstance(other, (NodeReturn)):
            return self.value == other.value
        else:
            return self.value == other