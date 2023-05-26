import subprocess
import shlex
import select
import os

class NodeExecutor():
    from lodepy.nodes.node_return import NodeReturn
    from lodepy.nodes.node import Node
    from lodepy.tasks.task import Task
    
    '''
    Class to execute tasks on a node
    '''
    def __init__(self, ssh: str) -> None:
        self.ssh = ssh

    def execute_task(self, task: Task, node: Node) -> 'NodeReturn':
        '''
        execute a Task. Need to format the task before I can really think of how to use it
        '''
        return task.execute(node)

    def send_command(self, cmd: str, read_size=25, ssh=True) -> str:
        '''
        Send a command, returns the prompt result
        '''

        if ssh:
          cmd = f'ssh {self.ssh} {cmd}'

        passed_cmd = shlex.split(cmd)

        process = subprocess.Popen(passed_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout = b''
        stderr = b''

        while process.poll() is None:
            ready, wait, exceptions = select.select([process.stdout, process.stderr], [], [process.stdout, process.stderr], 1)

            if process.stdout in ready:
                data = os.read(process.stdout.fileno(), read_size)
                stdout += data
            if process.stderr in ready:
                data = os.read(process.stderr.fileno(), read_size)
                stderr += data

            if not process.stderr and not process.stdout and process.poll() is None:
                process.wait()

        if process.stderr:
            data = os.read(process.stderr.fileno(), read_size)
            stderr += data

        if process.stdout:
            data = os.read(process.stdout.fileno(), read_size)
            stdout += data

        return process.returncode, stdout.decode('utf-8'), stderr.decode('utf-8')

    