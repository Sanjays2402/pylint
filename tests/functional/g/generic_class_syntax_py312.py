# pylint: disable=missing-docstring,too-few-public-methods
class Entity[_T: float]:
    last_update: int | None = None

    def __init__(self, data: _T) -> None:
        self.data = data


class Sensor(Entity[int]):
    def __init__(self, data: int) -> None:
        super().__init__(data)

    def async_update(self) -> None:
        self.data = 2

        if self.last_update is None:
            pass
        self.last_update = 2


class Switch(Entity[int]):
    def __init__(self, data: int) -> None:
        Entity.__init__(self, data)


class Parent[_T]:
    def __init__(self):
        self.update_interval = 0


class Child[_T](Parent[_T]):
    def func(self):
        self.update_interval = None


# Calling a type parameter infers to a TypeVar, which has no qname().
# https://github.com/pylint-dev/pylint/issues/11058
type Alias[_U] = None

_ = _U()  # [not-callable]
