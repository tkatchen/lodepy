from abc import abstractmethod
from typing import TypeVar

from lodepy.nodes.node_executor import NodeExecutor
from lodepy.nodes.node_return import NodeReturn

K = TypeVar('K')

class Task: # Note, a task should be able to execute a task using node_executor and then use the NodeReturn for comparisons.
    '''
    An abstract class for Tasks that can be run on Nodes
    '''
    @abstractmethod
    def execute(self, node_executor: NodeExecutor) -> 'NodeReturn[K]':
        '''
        The method to run when the task gets executed
        '''
