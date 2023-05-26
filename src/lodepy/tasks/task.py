from abc import abstractmethod
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
  from lodepy.nodes.node import Node
  from lodepy.nodes.node_return import NodeReturn

K = TypeVar('K')

class Task:
    '''
    An abstract class for Tasks that can be run on Nodes
    '''
    @abstractmethod
    def execute(node: 'Node') -> 'NodeReturn[K]':
        '''
        The method to run when the task gets executed
        '''
