class NodeVariables():
    '''
    The location to store node dependent information.

    This data is non-persistant and will be deleted on completion
    '''
    def __init__(self):
        self.dict: dict[str,any] = {}

    def flush(self):
        '''
        Clears all the information in the NodeVariables
        '''
        self.dict = {}

    def get(self, key: str, default=None):
        '''
        Get a value from the NodeVariables
        '''
        if key in self.dict:
            return self.dict[key]
        else:
            return default

    def set(self, key: str, value):
        '''
        Set a value
        '''
        self.dict[key] = value

    def __contains__(self, key):
        return key in self.dict

    def __getattribute__(self, name: str) -> any:
        return self.get(name)

    def __setattr__(self, name: str, value: any) -> None:
        self.set(name, value)