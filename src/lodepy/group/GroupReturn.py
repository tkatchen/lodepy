from typing import Callable, List, TypeVar

from lodepy.group.Group import Group
from lodepy.nodes.NodeReturn import NodeReturn

K = TypeVar('K')

class GroupReturn(Group):
    def __init__(self, values: List[NodeReturn[K]]) -> None:
        super([value. for value in values])
        self.values = values

        self.idx = 0

    def __iter__(self) -> None:
        self.idx = 0
        return self

    def __next__(self) -> NodeReturn[K]:
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