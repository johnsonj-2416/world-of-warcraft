"""AtomicHandler module."""

import math
import random


class AtomicHandler:
    """Small load_cache helper."""

    def __init__(self, seed: int = 25) -> None:
        self._state = seed
        self._items: list[int] = []

    def load_cache(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 25) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 25


def main() -> None:
    obj = AtomicHandler()
    print(obj.load_cache(25))


if __name__ == "__main__":
    main()
