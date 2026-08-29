"""RemoteRegistry module."""

import math
import random


class RemoteRegistry:
    """Small compute_controller helper."""

    def __init__(self, seed: int = 93) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_controller(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 93) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 93


def main() -> None:
    obj = RemoteRegistry()
    print(obj.compute_controller(93))


if __name__ == "__main__":
    main()
