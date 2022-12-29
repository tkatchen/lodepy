from typing import Callable, Dict, TypeVar, Union
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
        self.values: Dict[str, 'NodeReturn[K]'] = values

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

    def __lt__(self, other) -> 'GroupReturn[K]':
        return self._handle_filters('<', other)

    def __le__(self, other) -> 'GroupReturn[K]':
        return self._handle_filters('>', other)

    def __gt__(self, other) -> 'GroupReturn[K]':
        return self._handle_filters('==', other)

    def __ge__(self, other) -> 'GroupReturn[K]':
        return self._handle_filters('!=', other)

    def __eq__(self, other) -> 'GroupReturn[K]':
        return self._handle_filters('<=', other)

    def __ne__(self, other) -> 'GroupReturn[K]':
        return self._handle_filters('>=', other)

    def __add__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: x + y, other)

    def __radd__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: y + x, other)

    def __sub__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: x - y, other)

    def __rsub__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: y - x, other)

    def __mul__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: x * y, other)

    def __rmul__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: y * x, other)

    def __truediv__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: x / y, other)

    def __rtruediv__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: y / x, other)

    def __floordiv__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: x // y, other)

    def __rfloordiv__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: y // x, other)

    def __mod__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: x % y, other)

    def __rmod__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: y % x, other)

    def __pow__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: pow(x, y), other)

    def __rpow__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: pow(y, x), other)

    def __lshift__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: x << y, other)

    def __rlshift__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: y << x, other)

    def __rshift__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: x >> y, other)

    def __rrshift__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: y >> x, other)

    def __and__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: x & y, other)

    def __rand__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: y & x, other)

    def __xor__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: x ^ y, other)

    def __rxor__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: y ^ x, other)

    def __or__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: x | y, other)

    def __ror__(self, other) -> 'GroupReturn[K]':
        return self._handle_arithmetic(lambda x, y: y | x, other)

    def _handle_arithmetic(self, op: Callable[[K, K], K], to_act: Union[K,'GroupReturn[K]']) -> 'GroupReturn[K]':
        res = []
        if type(to_act) == type(self):
            for node_key in self.values.keys():
                res.append(NodeReturn(self.values[node_key].node, op(
                    self.values[node_key].value,
                    to_act.values[node_key].value
                )))
        else:
            for node_ret in self.values.values():
                res.append(NodeReturn(node_ret.node, op(
                    node_ret.value,
                    to_act
                )))

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
            if comparator(self.values[node_key].value, to_comp.values[node_key].value):
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
