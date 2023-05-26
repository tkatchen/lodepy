from typing import Callable, Dict, Generic, Set, TypeVar, Union
from lodepy.core.comparable import Comparable
from lodepy.core.operable import Operable
from lodepy.groups.group import Group
from lodepy.handling.lodepy_error import LodepyInvalidComparison
from lodepy.nodes.node import Node
from lodepy.nodes.node_return import NodeReturn
from lodepy.tasks.task import Task


K = TypeVar('K')

class GroupReturn(Group, Comparable['GroupReturn[K]'], Operable['GroupReturn[K]'], Generic[K]):
    '''
    The group return from executing a certain Task
    '''
    def __init__(self, values: Dict[str, 'NodeReturn[K]']) -> None:
        super(GroupReturn, self).__init__(name='group_return', nodes=set(values.values()))
        self.comp = self._handle_filters
        self.op_fn = self._handle_arithmetic
        self.values: Dict[str, 'NodeReturn[K]'] = values

    '''
    To-Do: need to find a way to iterate through values. Maybe just delete?

    def __iter__(self) -> 'Iterator[NodeReturn[K]]':
        self.idx = 0
        return self

    def __next__(self) -> 'NodeReturn[K]':
        if self.idx < len(self.values):
            res = self.values[self.idx]
            self.idx += 1
            return res
        else:
            raise StopIteration
    '''

    def _handle_arithmetic(self, op: Callable[[K, K], K], to_act: Union[K,'GroupReturn[K]']) -> 'GroupReturn[K]':
        res = {}
        if type(to_act) == type(self):
            for node_key in self.values.keys():
                res[node_key] = NodeReturn(self.values[node_key], op(
                    self.values[node_key].value,
                    to_act.values[node_key].value
                ))
        else:
            for node_ret in self.values.values():
                res[node_ret.name] = NodeReturn(node_ret, op(
                    node_ret.value,
                    to_act
                ))

        return GroupReturn(res)


    def _handle_filters(self, op: str, to_comp: Union[K,'GroupReturn[K]']) -> 'GroupReturn[K]': 
        '''
        Handler function for the filters from comparisons.
        '''
        if type(to_comp) == type(self):
            if op == '<': return self.filter_group_return(lambda x, to_comp: x < to_comp, to_comp)
            elif op == '>': return self.filter_group_return(lambda x, to_comp: x > to_comp, to_comp)
            elif op == '==': return self.filter_group_return(lambda x, to_comp: x == to_comp, to_comp)
            elif op == '!=': return self.filter_group_return(lambda x, to_comp: x != to_comp, to_comp)
            elif op == '<=': return self.filter_group_return(lambda x, to_comp: x <= to_comp, to_comp)
            elif op == '>=': return self.filter_group_return(lambda x, to_comp: x >= to_comp, to_comp)
            else: raise LodepyInvalidComparison(op)
                

        if op == '<': return self.filter(lambda x: x < to_comp)
        elif op == '>': return self.filter(lambda x: x > to_comp)
        elif op == '==': return self.filter(lambda x: x == to_comp)
        elif op == '!=': return self.filter(lambda x: x != to_comp)
        elif op == '<=': return self.filter(lambda x: x <= to_comp)
        elif op == '>=': return self.filter(lambda x: x >= to_comp)
        else: raise LodepyInvalidComparison(op)

    def filter_group_return(self, comparator, to_comp: 'GroupReturn[K]'):
        '''
        Filter the group return using a comparator with another group return.
        '''
        res = {}

        for node_key in self.values.keys():
            if node_key in to_comp.values and comparator(self.values[node_key].value, to_comp.values[node_key].value):
                res[node_key] = self.values[node_key]

        return GroupReturn(res)

    def filter(self, comparator: Callable[[K],bool]):
        '''
        Filter the group return using a comparator
        '''
        res = {}
        for node_ret in self.values.values():
            if comparator(node_ret.value):
                res[node_ret.name] = node_ret

        return GroupReturn(res)