from lodepy.data.data_store import DataStore

class lodepy(): # pylint: disable=invalid-name
    '''
    The static accessor to all of lodepy
    '''
    data_store: DataStore = None

    @classmethod
    def init(cls, data_dir: str, file_name:str):
        '''
        Initialize the static lodepy instance
        '''
        cls.data_store = DataStore(data_dir, file_name)

def init(data_dir: str, file_name: str) -> None:
    '''
    Initialize the lodepy instance

    Parameters:
        data_dir (str): The directory to pull the saved data store from.
        file_name (str): The name of the file to pull the data store from.
    '''
    lodepy.init(data_dir, file_name)

def data_store() -> DataStore:
    '''
    Access the lodepy data store

    Returns:
        (DataStore): The static data store for the lodepy instance
    '''
    return lodepy.data_store
