import json
from typing import Dict, List, Union
from lodepy.group.Group import Group
from lodepy.handling.LodepyError import LodepyDataSaveError

from lodepy.handling.LogManager import LogManager
from lodepy.nodes.Node import Node

class DataStore():
    '''
    The location of the cached data for the entire lodepy instances.

    The major difference between the DataStore and the NodeInformation is that
    the DataStore is used for variables that are refrenced among the multiple hosts.
    Meanwhile, the NodeInformation is independent for each host.

    Functionally, this is a dictionary with information that can be utilized by any host.
    '''
    def __init__(self, data_dir: str, file_name='.') -> None:
        self.data_dir = data_dir
        self.file_name = file_name
        data, nodes, groups = self._loadData()
        self.data : Dict[str, any]= {} if data is None else data
        self.nodes : Dict[str, Node] = {} if nodes is None else nodes
        self.groups : Dict[str, Group]= {} if groups is None else groups

    def _loadData(self):
        if self.data_dir[-1] == '/':
            self.data_dir = self.data_dir[:-1]

        try:
            with open(f'{self.data_dir}/{self.file_name}', encoding='utf-8') as file:
                json_data = json.load(file)
                return self._deserialize(json_data)
        except OSError:
            LogManager.addLog(
                f"Unable to locate saved data store at {self.data_dir}/{self.file_name}. Made new."
            )
            return {}

    def _deserialize(self, serialized_data):
        data = serialized_data['data']
        nodes = {}
        for node in serialized_data['nodes']:
            nodes[node[0]] = Node(node[0], node[1])

        groups = {}
        for name, group in serialized_data['groups'].values():
            group_nodes = set([])
            for node in group:
                group_nodes.add(Node(node[0], node[1]))
            groups[name] = Group(name, group_nodes)

        return data, nodes, groups

    def _serialize(self):
        nodes = [(node.name, node.ssh) for node in self.nodes.values()]
        groups = {}
        for group in self.groups.values():
            groups[group.name] = [(node.name, node.ssh) for node in list(group.nodes)]
        return {
            'data' : self.data,
            'nodes' : nodes,
            'groups' : groups
        }

    def writeData(self):
        json_string = self._serialize()
        try:
            with open(f'{self.data_dir}/{self.file_name}', 'w', encoding='utf-8') as file:
                json.dump(json_string, file)
        except OSError as exc:
            raise LodepyDataSaveError(f'{self.data_dir}/{self.file_name}') from exc

    def add_node(self, node: Node, group: Union[str, List[str]]):
        if type(group) == type([]):
            for g in group:
                if g in self.groups:
                    self.groups[g].add_node(node)
                else:
                    self.groups[g] = Group(g, set([node]))
        else:
            if group in self.groups:
                self.groups[group].add_node(node)
            else:
                self.groups[group] = Group(g, set([node]))

    def add_group(self, group: str, node: Union[Node, List[Node]]):
        if type(node) == type([]):
            self.groups[group] = Group(group, set(node))
        else:
            self.groups[group] = Group(group, set([node]))
