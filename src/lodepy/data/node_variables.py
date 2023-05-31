from typing import Any, Dict

from lodepy.handling.log_manager import LogManager


class NodeVariables():
    '''
    The location to store node dependent information.

    This data is non-persistant and will be deleted on completion
    '''
    def __init__(self):
        self.dict: Dict[str, Any] = {}

    def __getitem__(self, __name: str) -> Any:
        return self.dict[__name]

    def __setitem__(self, __name: str, __value: Any) -> None:
        self.dict[__name] = __value

    def __delitem__(self, __name: str) -> None:
        del self.dict[__name]

    def __missing__(self, __name: str) -> None:
        LogManager.add_log(
            f'Tried accessing {__name} from node variables while the key does not exist'
            )
        return None

    def __contains__(self, __name):
        return __name in self.dict

    def flush(self):
        '''
        Clears all the information in the NodeVariables
        '''
        self.dict = {}

    def get(self, key: str, default=None):
        '''
        Get a value from the NodeVariables

        :key: The key to get
        '''
        if key in self.dict:
            return self.dict[key]
        else:
            return default

    def set(self, key: str, value):
        '''
        Set a value

        :key: The key to set
        :value: The value to set at that key
        '''
        self.dict[key] = value
        