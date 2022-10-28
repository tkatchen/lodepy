from lodepy.data.DataStore import DataStore

class lodepy(): # pylint: disable=invalid-name
    '''
    The static accessor to all of lodepy
    '''
    data_store: DataStore = None
    
    @classmethod
    def init(cls, data_dir, file_name):
        cls.data_store = DataStore(data_dir, file_name)

def init(data_dir, file_name):
    lodepy.init(data_dir, file_name)

def data_store():
    return lodepy.data_store