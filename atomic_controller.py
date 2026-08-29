"""AtomicController module."""

import math
import random


class AtomicController:
    """Small parse_loader helper."""

    def __init__(self, seed: int = 79) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_loader(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 79) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 79


def main() -> None:
    obj = AtomicController()
    print(obj.parse_loader(79))


if __name__ == "__main__":
    main()
