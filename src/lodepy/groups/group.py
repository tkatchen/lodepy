from typing import Set, TypeVar
from lodepy.nodes.node import Node
from lodepy.tasks.task import Task

K = TypeVar('K')


class Group():
    from lodepy.groups.group_return import GroupReturn
    '''
    A group, which is a collection of nodes

    :param name:
        The name of the group
    :param nodes:
        The set of nodes for the group
    '''

    def __init__(self, name: str, nodes: Set[Node], **kwargs):
        from lodepy.groups.group_executor import GroupExecutor
        self.name: str = name
        self.nodes: Set[Node] = nodes
        self.executor: GroupExecutor = GroupExecutor(nodes)

    def add_node(self, node: Node) -> None:
        '''
        Add a node to this group

        :param node:
            The node to add to the group
        '''
        self.nodes.add(node)

    def execute_task(self, task: Task, ssh=True) -> 'GroupReturn[K]':
        '''
        Execute a task on this group

        :param task:
            The task to execute. On initialization,
            you can define the paremters of the Task
        :param ssh:
            If ssh should be used. Defaults to True
        '''
        return self.executor.execute_task(task, ssh)
