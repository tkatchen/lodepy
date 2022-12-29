from abc import abstractmethod

from lodepy.nodes.node import Node

class Task:
    '''
    An abstract class for Tasks that can be run on Nodes
    '''
    @abstractmethod
    def execute(self, node: Node) -> None:
        '''
        The method to run when the task gets executed
        '''
