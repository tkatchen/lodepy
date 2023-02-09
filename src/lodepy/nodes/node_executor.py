import subprocess

from lodepy.tasks.task import Task

class NodeExecutor():
    from nodes.node_return import NodeReturn
    '''
    Class to execute tasks on a node
    '''
    def __init__(self, ssh: str) -> None:
        self.ssh = ssh
        
        self.connection = self._create_connection()


    def _create_connection(self) -> any: # This can / should be updated to some subprocess class in the future
        '''
        create an ssh connection and update some local var
        '''

    def execute_task(task: Task) -> 'NodeReturn':
        '''
        execute a Task. Need to format the task before I can really think of how to use it
        '''

    def send_command(cmd: str) -> str:
        '''
        Send a command, returns the prompt result
        '''

    