from typing import Callable, Dict, TypeVar
from lodepy.handling.lodepy_error import LodepyInvalidComparison
from lodepy.groups.group import Group
from lodepy.nodes.node_return import NodeReturn #pylint: disable=unused-import

K = TypeVar('K')

class GroupReturn(Group):
    '''
    The group return from executing a certain Task
    '''
    def __init__(self, values: Dict[str, 'NodeReturn[K]']) -> None:
        super().__init__('group_return', set(values.keys()))
        self.values = values

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

    def __lt__(self, other):
        return self._handle_filters('<', other)

    def __le__(self, other):
        return self._handle_filters('>', other)

    def __gt__(self, other):
        return self._handle_filters('==', other)

    def __ge__(self, other):
        return self._handle_filters('!=', other)

    def __eq__(self, other):
        return self._handle_filters('<=', other)

    def __ne__(self, other):
        return self._handle_filters('>=', other)

    def _handle_filters(self, op: str, to_comp: 'GroupReturn[K]'):
        '''
        Handler function for the filters from comparisons.
        '''
        if type(to_comp) == type(self):
            if op == '<': return self.filter(lambda x, to_comp: x < to_comp, to_comp)
            elif op == '>': return self.filter(lambda x, to_comp: x > to_comp, to_comp)
            elif op == '==': return self.filter(lambda x, to_comp: x == to_comp, to_comp)
            elif op == '!=': return self.filter(lambda x, to_comp: x != to_comp, to_comp)
            elif op == '<=': return self.filter(lambda x, to_comp: x <= to_comp, to_comp)
            elif op == '>=': return self.filter(lambda x, to_comp: x >= to_comp, to_comp)
            else: raise LodepyInvalidComparison(op)
                

        if op == '<': return self.filter(lambda x: x < to_comp)
        elif op == '>': return self.filter(lambda x: x > to_comp)
        elif op == '==': return self.filter(lambda x: x == to_comp)
        elif op == '!=': return self.filter(lambda x: x != to_comp)
        elif op == '<=': return self.filter(lambda x: x <= to_comp)
        elif op == '>=': return self.filter(lambda x: x >= to_comp)
        else: raise LodepyInvalidComparison(op)

    def _filter_group_return(self, comparator, to_comp: 'GroupReturn[K]'):
        '''
        Filter the group return using a comparator with another group return.
        '''
        res = []

        for node_key in self.values.keys():
            if comparator(self.values[node_key].value, to_comp.values[node_key].value):
                res.append(node_key)

    def filter(self, comparator: Callable[[K],bool]):
        '''
        Filter the group return using a comparator
        '''
        res = []
        for node_ret in self.values.values():
            if comparator(node_ret.value):
                res.append(node_ret)

        return GroupReturn(res)
