from abc import abstractmethod
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from lodepy.nodes.node import Node
    from lodepy.nodes.node_return import NodeReturn

K = TypeVar('K')


class Task(Generic[K]):
    '''
    The class for Tasks that can be run on Nodes
    '''

    def __init__(self, **kwargs) -> None:
        self.ssh : bool = True
        if 'ssh' in kwargs:
            self.ssh = kwargs['ssh']

    @abstractmethod
    def execute(node: 'Node', **kwargs) -> 'NodeReturn[K]':
        '''
        The method to run when the task gets executed
        '''
