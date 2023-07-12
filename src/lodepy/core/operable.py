from typing import Callable, Generic, TypeVar

T = TypeVar('T')


class Operable(Generic[T]):
    '''
    A class that can be extended, allowing the child to become operable
    '''

    def __init__(self) -> None:
        self.op_fn: Callable
        super().__init__()

    def __and__(self, other) -> T:
        return self.op_fn(lambda x, y: x & y, other)

    def __rand__(self, other) -> T:
        return self.op_fn(lambda x, y: y & x, other)

    def __xor__(self, other) -> T:
        return self.op_fn(lambda x, y: x ^ y, other)

    def __rxor__(self, other) -> T:
        return self.op_fn(lambda x, y: y ^ x, other)

    def __or__(self, other) -> T:
        return self.op_fn(lambda x, y: x | y, other)

    def __ror__(self, other) -> T:
        return self.op_fn(lambda x, y: y | x, other)

    def __add__(self, other) -> T:
        return self.op_fn(lambda x, y: x + y, other)

    def __radd__(self, other) -> T:
        return self.op_fn(lambda x, y: y + x, other)

    def __sub__(self, other) -> T:
        return self.op_fn(lambda x, y: x - y, other)

    def __rsub__(self, other) -> T:
        return self.op_fn(lambda x, y: y - x, other)

    def __mul__(self, other) -> T:
        return self.op_fn(lambda x, y: x * y, other)

    def __rmul__(self, other) -> T:
        return self.op_fn(lambda x, y: y * x, other)

    def __truediv__(self, other) -> T:
        return self.op_fn(lambda x, y: x / y, other)

    def __rtruediv__(self, other) -> T:
        return self.op_fn(lambda x, y: y / x, other)

    def __floordiv__(self, other) -> T:
        return self.op_fn(lambda x, y: x // y, other)

    def __rfloordiv__(self, other) -> T:
        return self.op_fn(lambda x, y: y // x, other)

    def __mod__(self, other) -> T:
        return self.op_fn(lambda x, y: x % y, other)

    def __rmod__(self, other) -> T:
        return self.op_fn(lambda x, y: y % x, other)

    def __pow__(self, other) -> T:
        return self.op_fn(lambda x, y: pow(x, y), other)

    def __rpow__(self, other) -> T:
        return self.op_fn(lambda x, y: pow(y, x), other)

    def __lshift__(self, other) -> T:
        return self.op_fn(lambda x, y: x << y, other)

    def __rlshift__(self, other) -> T:
        return self.op_fn(lambda x, y: y << x, other)

    def __rshift__(self, other) -> T:
        return self.op_fn(lambda x, y: x >> y, other)

    def __rrshift__(self, other) -> T:
        return self.op_fn(lambda x, y: y >> x, other)

    def __and__(self, other) -> T:
        return self.op_fn(lambda x, y: x & y, other)

    def __rand__(self, other) -> T:
        return self.op_fn(lambda x, y: y & x, other)

    def __xor__(self, other) -> T:
        return self.op_fn(lambda x, y: x ^ y, other)

    def __rxor__(self, other) -> T:
        return self.op_fn(lambda x, y: y ^ x, other)

    def __or__(self, other) -> T:
        return self.op_fn(lambda x, y: x | y, other)

    def __ror__(self, other) -> T:
        return self.op_fn(lambda x, y: y | x, other)
