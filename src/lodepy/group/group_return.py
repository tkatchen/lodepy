from typing import Callable, List, TypeVar

from lodepy.group.group import Group
from lodepy.nodes.node_return import NodeReturn #pylint: disable=unused-import

K = TypeVar('K')

class GroupReturn(Group):
    '''
    The group return from executing a certain Task
    '''
    def __init__(self, values: List['NodeReturn[K]']) -> None:
        super().__init__('group_return', set(values))
        self.values = values

        self.idx = 0

    def __iter__(self) -> None:
        self.idx = 0
        return self

    def __next__(self) -> 'NodeReturn[K]':
        if self.idx < len(self.values):
            res = self.values[self.idx]
            self.idx += 1
            return res
        else:
            raise StopIteration

    def filter(self, comparator: Callable[[K],bool]):
        '''
        Filter the group using a comparator
        '''
        res = []
        for value in self.values:
            if comparator(value):
                res.append(value)

        return GroupReturn(res)
