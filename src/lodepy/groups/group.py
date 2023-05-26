from typing import Set
from lodepy.nodes.node import Node
from lodepy.tasks.task import Task

class Group():
    '''
    A group, which is a collection of nodes
    '''
    def __init__(self, name: str, nodes: Set[Node], **kwargs):
        from lodepy.groups.group_executor import GroupExecutor
        
        self.name: str = name
        self.nodes: Set[Node] = nodes
        self.executor: GroupExecutor = GroupExecutor(nodes)

    def add_node(self, node: Node) -> None:
        '''
        Add a node to this group
        '''
        self.nodes.add(node)

    def execute_task(self, task: Task):
        '''
        Execute a task on this group
        '''
        return self.executor.execute_task(task)