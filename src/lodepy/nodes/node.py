from typing import List
from lodepy.data.node_variables import NodeVariables
from lodepy.tasks.general.get_info import GetInfo
from lodepy.handling.lodepy_error import LodepyHostNotReached

class Node():
    '''
    The instance of the node that is used for task execution
    '''

    def __init__(self, name: str, ssh: str) -> None:
        from lodepy.nodes.node_executor import NodeExecutor

        self.name = name
        self.ssh = ssh
        self.information = NodeVariables()
        self.executor = NodeExecutor(ssh)
        self.hostname: str = None
        self.chassis: str = None
        self.machine_id: str = None
        self.boot_id: str = None
        self.os: str = None
        self.kernel: str = None
        self.architecture: str = None

        self._collect_host_info()

    def _collect_host_info(self):
        _, _, err = self.executor.execute_task(GetInfo, self)
        if err:
            raise LodepyHostNotReached(self.name, self.ssh)

    def copy(self, copy: "Node"):
        '''
        Copy the node from another
        '''
        self.name = copy.name
        self.ssh = copy.ssh
        self.information = copy.information
        self.executor = copy.executor

    def __hash__(self) -> int:
        return self.ssh.__hash__() + self.name.__hash__()
