from typing import List, overload

from lodepy.data.NodeVariables import NodeVariables
import lodepy


class Node():
    '''
    The instance of the node that is used for task execution
    '''
    @overload
    def __init__(self, name: str, ssh: str, groups: List[str]) -> None:
        self.name = name
        self.ssh = ssh
        self.information = NodeVariables()

        for group in groups:
            lodepy.init()

    @overload
    def __init__(self, copy: "Node"):
        self.name = copy.name
        self.ssh = copy.ssh
        self.groups = copy.groups
        self.information = copy.information
    
    def __str__(self) -> str:
        return self.ssh