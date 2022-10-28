class LogManager():
    _logs = []

    @classmethod
    def addLog(cls, message:str):
        cls._logs.append(message)

    @classmethod
    def getLogs(cls):
        return '\n'.join(cls._logs)

    