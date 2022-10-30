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

        lodepy.data_store().add_node(self, groups)

    @overload
    def __init__(self, copy: "Node"):
        self.name = copy.name
        self.ssh = copy.ssh
        self.information = copy.information

    def __hash__(self) -> int:
        return self.ssh.__hash__() + self.name.__hash__()
