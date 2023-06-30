from typing import TypeVar
from lodepy.handling.log_error import LogError
from lodepy.nodes.node import Node
from lodepy.nodes.node_return import NodeReturn
from lodepy.tasks.task import Task
from lodepy.handling.log_manager import LogManager

K = TypeVar('K')

class GitStatus(Task):
    def __init__(self, **kwargs):
        self.ssh = True
        if 'ssh' in kwargs:
            self.ssh = kwargs['ssh']

    def execute(self, node: 'Node') -> 'NodeReturn[K]':
        res = node.executor.send_command('git status', ssh=self.ssh)

        if res[2] != '':
            LogManager.add_log(LogError('git status', res[2], node))

        return NodeReturn(node, res[1], res[0])
