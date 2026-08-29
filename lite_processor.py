"""LiteHandler module."""

import math
import random


class LiteHandler:
    """Small dispatch_registry helper."""

    def __init__(self, seed: int = 40) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_registry(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 40) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 40


def main() -> None:
    obj = LiteHandler()
    print(obj.dispatch_registry(40))


if __name__ == "__main__":
    main()
