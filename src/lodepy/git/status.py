from typing import TypeVar
from lodepy.nodes.node import Node
from lodepy.nodes.node_return import NodeReturn
from lodepy.tasks.task import Task

K = TypeVar('K')

class Status(Task):
    def execute(node: 'Node') -> 'NodeReturn[K]':
        res = node.executor.send_command('git status', ssh=False)
        print(res)