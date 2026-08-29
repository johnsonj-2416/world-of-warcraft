"""AtomicRegistry module."""

import math
import random


class AtomicRegistry:
    """Small build_loader helper."""

    def __init__(self, seed: int = 54) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_loader(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 54) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 54


def main() -> None:
    obj = AtomicRegistry()
    print(obj.build_loader(54))


if __name__ == "__main__":
    main()
