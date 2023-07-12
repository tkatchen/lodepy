from collections import deque
from lodepy.data.data_store import DataStore
from lodepy.groups.group import Group
from typing import Dict

from lodepy.nodes.node import Node


class Main():
    '''
    The static accessor to all of lodepy
    '''
    data_store: DataStore = None

    @classmethod
    def init(cls, data_dir: str, file_name: str):
        '''
        Initialize the static lodepy instance
        '''
        cls.data_store = DataStore(data_dir, file_name)


def init(data_dir: str, file_name: str) -> None:
    '''
    Initialize the lodepy instance

    :data_dir: The directory to pull the saved data store from.
    :file_name: The name of the file to pull the data store from.
    '''
    Main.init(data_dir, file_name)


def data_store() -> DataStore:
    '''
    Access the lodepy data store

    :return: The static data store for the lodepy instance
    '''
    return Main.data_store


def get_groups() -> Dict[str, Group]:
    '''
    Get the Groups from disk.

    The file is stored in /etc/lodepy/nodes.txt
    Should be the same format as the input for import_groups_txt

    :return: A dictionary from the groups name to the relative group
    '''
    return import_groups_txt('/etc/lodepy/nodes.txt')


def import_groups_txt(file_name: str) -> Dict[str, Group]:
    '''
    Import a series of groups from a formatted text file

    :file_name: The name of the file to pull data from

    :return: A dictionary from the groups name to the relative group
    '''

    res = {}

    cur_group: Group = None

    with open(file_name) as file:
        lines = [x[:-1] for x in file.readlines()]
        for cur in lines:
            # Empty line
            if len(cur) == 0:
                continue

            # Find new Group
            if cur.startswith('[') and cur.endswith(']'):
                if cur_group != None:
                    res[cur_group.name] = cur_group

                group_name = cur[1:-1]
                cur_group = Group(group_name, set())

            # Node found
            if cur_group == None:
                continue

            info = cur.split(',')
            if len(info) != 2:
                continue

            new_node = Node(info[0].strip(), info[1].strip())
            cur_group.add_node(new_node)

    if cur_group != None:
        res[cur_group.name] = cur_group

    return res
