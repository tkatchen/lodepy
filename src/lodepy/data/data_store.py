import json
from typing import Any, Dict, List, Tuple, Union
from lodepy.groups.group import Group
from lodepy.handling.lodepy_error import LodepyDataSaveError

from lodepy.handling.log_manager import LogManager
from lodepy.nodes.node import Node


class DataStore():
    '''
    The location of the cached data for the entire lodepy instances.

    The major difference between the DataStore and the NodeInformation is that
    the DataStore is used for variables that are refrenced among the multiple hosts.
    Meanwhile, the NodeInformation is independent for each host.

    Functionally, this is a dictionary with information that can be utilized by any host.

    :file_name: The name of the file to store in
    '''

    def __init__(self, file_name='/etc/lodepy/datastore.txt') -> None:
        self.file_name = file_name
        data, nodes, groups = self._load_data()
        self.data: Dict[str, any] = {} if data is None else data
        self.nodes: Dict[str, Node] = {} if nodes is None else nodes
        self.groups: Dict[str, Group] = {} if groups is None else groups

    def __getitem__(self, __name: str) -> Any:
        return self.data[__name]

    def __setitem__(self, __name: str, __value: Any) -> None:
        self.data[__name] = __value

    def __delitem__(self, __name: str) -> None:
        del self.data[__name]

    def __missing__(self, __name: str) -> None:
        LogManager.add_log(
            f'Tried accessing {__name} from data store while the key does not exist')
        return None

    def __contains__(self, __name):
        return __name in self.data

    def _load_data(self) -> Tuple[Dict[str, any], Dict[str, Node], Dict[str, Group]]:
        '''
        load the stored data from a saved state

        Returns:
            (Tuple[Dict[str, any], Dict[str, Node], Dict[str, Group]]): Tuple of all the saved data
                Index 0: The saved data/variables
                Index 1: The saved nodes
                Index 2: The saved groups
        '''
        if self.data_dir[-1] == '/':
            self.data_dir = self.data_dir[:-1]

        try:
            with open(f'{self.data_dir}/{self.file_name}', encoding='utf-8') as file:
                json_data = json.load(file)
                return self._deserialize(json_data)
        except OSError:
            LogManager.add_log(
                f"Unable to locate saved data store at {self.data_dir}/{self.file_name}. Made new."
            )
            return ({}, {}, {})

    def _deserialize(
        self, serialized_data: Dict[str, any]
    ) -> Tuple[Dict[str, any], Dict[str, Node], Dict[str, Group]]:
        '''
        Deserializes the data from the JSON file
        '''
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
        '''
        Serialize the data from the data store to put into a JSON file
        '''
        nodes = [(node.name, node.ssh) for node in self.nodes.values()]
        groups = {}
        for group in self.groups.values():
            groups[group.name] = [(node.name, node.ssh)
                                  for node in list(group.nodes)]
        return {
            'data': self.data,
            'nodes': nodes,
            'groups': groups
        }

    def write_data(self):
        '''
        Write the data to a JSON file
        '''
        json_string = self._serialize()
        try:
            with open(f'{self.data_dir}/{self.file_name}', 'w', encoding='utf-8') as file:
                json.dump(json_string, file)
        except OSError as exc:
            raise LodepyDataSaveError(
                f'{self.data_dir}/{self.file_name}') from exc

    def add_node(self, node: Node, group: Union[str, List[str]]):
        '''
        Add a node to (a) group(s)

        :node: The node to add
        :group: The group(s) to add to that node
        '''
        if isinstance(group, list):
            for cur in group:
                if cur in self.groups:
                    self.groups[cur].add_node(node)
                else:
                    self.groups[cur] = Group(cur, set([node]))
        else:
            if group in self.groups:
                self.groups[group].add_node(node)
            else:
                self.groups[group] = Group(group, set([node]))

    def add_group(self, group: str, node: Union[Node, List[Node]]):
        '''
        Add a group with node(s)

        :group: The group to add
        :node: The node(s) to add to that group
        '''
        if isinstance(node, list):
            self.groups[group] = Group(group, set(node))
        else:
            self.groups[group] = Group(group, set([node]))
