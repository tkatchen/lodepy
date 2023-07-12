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
    '''
    Error thrown for when lodepy is unable to access a host
    '''

    def __init__(self, host_name: str, host_addr: str) -> None:
        super().__init__(
            f'lodepy was unable to access host {host_name} at {host_addr}')


class LodepyDataSaveError(LodepyError):
    '''
    Error thrown when lodepy is unable to save data
    '''

    def __init__(self, file_path: str):
        super().__init__(f'lodepy failed to save data to {file_path}')


class LodepyInvalidComparison(LodepyError):
    '''
    Errow thrown when trying to compare using an unknown comparator
    '''

    def __init__(self, comparator: str):
        super().__init__(
            f'lodepy failed to compare using the comparator {comparator}')


class LodepyInvalidCompareType(LodepyError):
    '''
    Can not compare two uncomparable types
    '''

    def __init__(self, base: str, to_comp: str):
        super().__init__(
            f'lodepy failed to compare type {base} with {to_comp}')
