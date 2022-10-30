class LogManager():
    '''
    A class with static methods to manage logs
    '''
    _logs = []

    @classmethod
    def add_log(cls, message:str):
        '''
        Add a log to the lodepy log manager
        '''
        cls._logs.append(message)

    @classmethod
    def get_logs(cls):
        '''
        Get the current logs
        '''
        return '\n'.join(cls._logs)
