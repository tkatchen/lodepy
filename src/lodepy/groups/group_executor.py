from typing import Dict, Set
from lodepy.groups.group_return import GroupReturn
from lodepy.nodes.node import Node
from lodepy.nodes.node_return import NodeReturn
from lodepy.tasks.task import Task


class GroupExecutor():
    def __init__(self, nodes: Set[Node]) -> None:
        self.nodes = nodes

    def execute_task(self, task: Task):
        res : Dict['str', 'NodeReturn'] = {}

        for node in list(self.nodes):
            response = node.executor.execute_task(task, node)
            
            res[node.name] = response

        return GroupReturn(res)