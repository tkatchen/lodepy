from typing import TypeVar, Union
from lodepy.handling.lodepy_error import LodepyInvalidComparison

from lodepy.nodes.node import Node
from lodepy.core.comparable import Comparable
K = TypeVar('K')


class NodeReturn(Node, Comparable):
    '''
    The return of a task executed on a certain node.
    '''

    def __init__(self, node: Node, value: K, returncode: int):
        # pylint: disable=super-init-not-called
        super(NodeReturn, self).copy(node)
        self.value = value
        self.comp = self._handle_comp
        self.returncode = returncode

    def __str__(self) -> K:
        return str(self.value)

    def __eq__(self, other: 'NodeReturn') -> bool:
        if isinstance(other, (NodeReturn)):
            return self.value == other.value
        else:
            return self.value == other

    def _handle_comp(self, op: str, to_comp: Union[K, 'NodeReturn[K]']) -> bool:
        '''
        Handler function for the filters from comparisons.
        '''
        if type(to_comp) == type(self):
            if op == '<':
                return self.value < to_comp.value
            elif op == '>':
                return self.value > to_comp.value
            elif op == '==':
                return self.value == to_comp.value
            elif op == '!=':
                return self.value != to_comp.value
            elif op == '<=':
                return self.value <= to_comp.value
            elif op == '>=':
                return self.value >= to_comp.value
            else:
                raise LodepyInvalidComparison(op)

        if op == '<':
            return self.value < to_comp
        elif op == '>':
            return self.value > to_comp
        elif op == '==':
            return self.value == to_comp
        elif op == '!=':
            return self.value != to_comp
        elif op == '<=':
            return self.value <= to_comp
        elif op == '>=':
            return self.value >= to_comp
        else:
            raise LodepyInvalidComparison(op)

    def __hash__(self) -> int:
        return super().__hash__()
