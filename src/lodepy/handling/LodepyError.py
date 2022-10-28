class LodepyError(Exception):
    '''
    The base error class for lodepy
    '''

    def __init__(self, message: str) -> None:
        self.message = message
        super(LodepyError, self).__init__(self.message)
 
    def __str__(self) -> None:
        return f'lodepy encountered an error: \n\n{self.message}'

class LodepyHostNotReached(LodepyError):
    def __init__(self, host_name: str, host_addr: str) -> None:
        super().__init__(f'lodepy was unable to access host {host_name} at {host_addr}')

class LodepyDataSaveError(LodepyError):
    def __init__(self, file_path: str):
        super().__init__(f'lodepy failed to save data to {file_path}')