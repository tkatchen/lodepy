from lodepy.groups.group import GroupReturn
from lodepy.nodes.node import Node
from lodepy.nodes.node_return import NodeReturn
from typing import Set, Dict

from lodepy.tasks.task import Task


class GroupExecutor():
    def __init__(self, nodes: Set[Node]) -> None:
        self.nodes = nodes

    def execute_task(self, task: Task):
        res : Dict['str', 'NodeReturn']= {}

        for node in list(self.nodes):
            # To-Do execute_task should return a Node
            response = node.executor.execute_task(task)
            
            res[node.name] = NodeReturn(node, response)

        return GroupReturn(res)