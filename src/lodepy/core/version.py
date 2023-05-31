from typing import Union
from lodepy.core.comparable import Comparable
from lodepy.handling.lodepy_error import LodepyInvalidCompareType


class Version(Comparable):
    '''
    Class representation of a Version. Allows for easy comparison of versions (very helpful for package management)

    :version: The version number of the form a.b.c... for any number of ints
    :suffix: The suffix of the version (i.e. 1.0.0-a.1, the suffix would be a.1)
    '''
    def __init__(self, version: str, suffix: str=None) -> None:
        self._version = []

        for num in version.split('.'):
            self._version.append(int(num))

        self.suffix = suffix

    def comp(self, op, to_comp: Union[str,'Version']):
        buff = None
        if type(to_comp) == type(''):
            buff = to_comp.split('.')
        elif type(to_comp) == type(self):
            buff = to_comp._version
        else:
            raise LodepyInvalidCompareType(type(self), type(to_comp))
            
        # Honestly, trying to do lt and gt are a pain in the ass. Levels easier to just not with the opposite.    
        if op == '>':
            return not self.comp('<=', to_comp)
        if op == '<':
            return not self.comp('>=', to_comp)
        if op == '!=':
            return not self.comp('!=', to_comp)

        for i in range(len(buff)):
            if op == '==':
                if buff[i] == '*':
                    continue
                if int(buff[i]) != self._version[i]:
                    return False
            if op == '>=':
                if buff[i] == '*':
                    continue
                if self._version[i] > int(buff[i]):
                    return True
                if self._version[i] < int(buff[i]):
                    return False
            if op == '<=':
                if buff[i] == '*':
                    continue
                if self._version[i] < int(buff[i]):
                    return True
                if self._version[i] > int(buff[i]):
                    return False

        return True
            
