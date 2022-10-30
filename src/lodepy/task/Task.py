from abc import abstractmethod

class Task:
    '''
    An abstract class for Tasks that can be run on Nodes
    '''
    @abstractmethod
    def execute(self) -> None:
        '''
        The method to run when the task gets executed
        '''
