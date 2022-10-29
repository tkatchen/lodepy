import json
from typing import Dict, List, Union
from lodepy.group.Group import Group
from lodepy.handling.LodepyError import LodepyDataSaveError

from lodepy.handling.LogManager import LogManager
from lodepy.nodes.Node import Node

class DataStore():
    """
    The location of the cached data for the entire lodepy instances.

    The major difference between the DataStore and the NodeInformation is that
    the DataStore is used for variables that are refrenced among the multiple hosts.
    Meanwhile, the NodeInformation is independent for each host.

    Functionally, this is a dictionary with information that can be utalized by any host.
    """
    def __init__(self, data_dir: str, file_name='.') -> None:
        self.data_dir = data_dir
        self.file_name = file_name
        data, nodes, groups = self._loadData()
        self.data = {} if data is None else data
        self.nodes = {} if nodes is None else nodes
        self.groups : Dict[str, Group]= {} if groups is None else groups

    def _loadData(self):
        if self.data_dir[-1] == '/':
            self.data_dir = self.data_dir[:-1]

        try:
            with open(f'{self.data_dir}/{self.file_name}', encoding='utf-8') as file:
                json_data = json.load(file)
                return self._deserialize(json_data)
        except:
            LogManager.addLog(
                f"Unable to locate saved data store at {self.data_dir}/{self.file_name}. Made new."
            )
            return {}

    def _deserialize(self, serialized_data):
        return serialized_data['data'], serialized_data['nodes'], serialized_data['groups']

    def _serialize(self):
        return {
            'data' : self.data,
            'nodes' : self.nodes,
            'groups' : self.groups
        }

    def writeData(self):
        json_string = self._serialize()
        try:
            with open(f'{self.data_dir}/{self.file_name}', 'w', encoding='utf-8') as file:
                json.dump(json_string, file)
        except:
            raise LodepyDataSaveError(f'{self.data_dir}/{self.file_name}')

    def add_host(self, node: Node, group: Union[str, List[str]]):
        if type(group) == type([]):
            for g in group:
                if g in self.groups:
                    self.groups[g].add_node() = node.ssh
                else:
                    self.groups[g]
        else:
            self.groups[group][node.name] = node.ssh
