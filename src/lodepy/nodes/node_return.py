from typing import TypeVar

from lodepy.nodes.node import Node

K = TypeVar('K')

class NodeReturn(Node):
    '''
    The return of a task executed on a certain node.
    '''
    def __init__(self, node: Node, value: K, returncode: int):
        #pylint: disable=super-init-not-called
        super().copy(node)
        self.value = value
        self.returncode = returncode

    def __str__(self) -> K:
        return str(self.value)

    def __eq__(self, other: 'NodeReturn') -> bool:
        if isinstance(other, (NodeReturn)):
            return self.value == other.value
        else:
            return self.value == other

    def __hash__(self) -> int:
        return super().__hash__()