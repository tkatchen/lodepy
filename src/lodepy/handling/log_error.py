from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from lodepy.nodes.node import Node


class LogError():
    def __init__(self, task: str, message: str, node: 'Node') -> None:
        self.task = task
        self.message = message
        self.node = node

    def __str__(self):
        return f'''
!====ERROR====!
{self.task} failed on node {self.node}.

Message:
{self.message}
!=============!'''
