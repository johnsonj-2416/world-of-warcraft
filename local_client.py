"""FastManager module."""

import math
import random


class FastManager:
    """Small flush_collector helper."""

    def __init__(self, seed: int = 7) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_collector(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 7) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 7


def main() -> None:
    obj = FastManager()
    print(obj.flush_collector(7))


if __name__ == "__main__":
    main()
