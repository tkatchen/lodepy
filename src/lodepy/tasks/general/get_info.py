from lodepy.handling.log_error import LogError
from lodepy.nodes.node import Node
from lodepy.nodes.node_return import NodeReturn
from lodepy.tasks.task import Task
from lodepy.handling.log_manager import LogManager


class GetInfo(Task):
    def __init__(self, **kwargs):
        '''
        Get info on the current node. This Task doesn't return information.
        Instead it updates the values of the Node with the updated information.
        To access the return values, instead access the properties of the Node.
        '''

        super(**kwargs)

    def execute(self, node: 'Node') -> 'NodeReturn[str]':
        res = node.executor.send_command('hostnamectl', ssh=self.ssh)

        if res[2] != '':
            LogManager.add_log(LogError('hostnamectl', res[2], node))

        for line in res[2].split('\n'):
            k, v = line.split(':')
            
            if k.strip() == 'Static hostname'   : node.hostname = v.strip()
            if k.strip() == 'Chassis'           : node.chassis = v.strip()
            if k.strip() == 'Machine ID'        : node.machine_id = v.strip()
            if k.strip() == 'Boot ID'           : node.boot_id = v.strip()
            if k.strip() == 'Operating System'  : node.os = v.strip()
            if k.strip() == 'Kernel'            : node.kernel = v.strip()
            if k.strip() == 'Architecture'      : node.architecture = v.strip()
        

        return NodeReturn(node, 'ok', res[0])
