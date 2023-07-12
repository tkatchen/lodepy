from lodepy.handling.log_error import LogError
from lodepy.nodes.node import Node
from lodepy.nodes.node_return import NodeReturn
from lodepy.core.version import Version
from lodepy.tasks.task import Task
from lodepy.handling.log_manager import LogManager


class GitVersion(Task):
    def __init__(self, **kwargs):
        super(**kwargs)

    def execute(self, node: 'Node') -> 'NodeReturn[Version]':
        res = node.executor.send_command('git version', ssh=self.ssh)

        if res[2] != '':
            LogManager.add_log(LogError('git version', res[2], node))

        return NodeReturn(node, Version(res[1].split(' ')[2].strip()), res[0])
