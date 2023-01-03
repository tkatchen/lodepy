from typing import List, overload

from lodepy.data.node_variables import NodeVariables


class Node():
    '''
    The instance of the node that is used for task execution
    '''
    def __init__(self, name: str, ssh: str, groups: List[str]) -> None:
        self.name = name
        self.ssh = ssh
        self.information = NodeVariables()

    def copy(self, copy: "Node"):
        self.name = copy.name
        self.ssh = copy.ssh
        self.information = copy.information

    def __hash__(self) -> int:
        return self.ssh.__hash__() + self.name.__hash__()
