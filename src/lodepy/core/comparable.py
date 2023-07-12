from typing import Callable, Generic, TypeVar

T = TypeVar('T')


class Comparable(Generic[T]):
    '''
    A class that can be extended, allowing the child to become comparable
    '''

    def __init__(self) -> None:
        self.comp: Callable
        super().__init__()

    def __lt__(self, other) -> T:
        return self.comp('<', other)

    def __le__(self, other) -> T:
        return self.comp('<=', other)

    def __gt__(self, other) -> T:
        return self.comp('>', other)

    def __ge__(self, other) -> T:
        return self.comp('>=', other)

    def __eq__(self, other) -> T:
        return self.comp('==', other)

    def __ne__(self, other) -> T:
        return self.comp('!=', other)
